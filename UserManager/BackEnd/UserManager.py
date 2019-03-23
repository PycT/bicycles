import os;
import sys;
import hashlib;
import datetime;

current_dir = os.path.dirname(__file__);
current_absolute_path = os.path.abspath(current_dir);
db_manager_package_path = current_absolute_path + "/../../DBManager";
sys.path.append(db_manager_package_path);

from DBManager import DBManager;

"""
 User Data Document Structure:

{
 "email": "vasya@pupkin.com",
 "password": "9834akjfhkfbzb#$hash",
 "name": "vasya",
 "date.creation": "1841-03-12 22:33:44",
 "date.update.last": 22-01-2019 03:03:03",
 "status": "ok",
 "field.utility": "pew-pew!" 
}

"email" field is also used as login.
"""


class UserManager:
"""User data is always should be passed as dictionary!"""
	def __init__(self):

		self.db = DBManager("mongodb", 27017);
		self.db.setDB("usersDB");
		self.db.setCollection("users_records");

		self.name = "Bruce Wayne";
		self.pwdhash = "";
		self.email = "my@email.com";
		self.creation_date = None;
		self.update_date = None;
		self.status = "pending";
		self.authenticated = False;
		self.role = None;

	def makeHash(self, i_str):

		sha512 = hashlib.new('sha512');
		sha512.update(i_str.encode('utf-8'));
		return sha512.hexdigest();

	def getTimeStamp(self):
		"""
		Returns a string of timestamp.
		"""

		time_stamp = datetime.datetime.now();

		return str(time_stamp);

	def isEmailUsed(self, email):
		"""
		A check if email entered when registering is already in use.
		"""

		testq = {"email": email};
		test_result = self.db.request("getOne", testq);

		if test_result:
			return True;
		else:
			return False;

	def create(self, user_data): #user_data is a dictionary
		"""
		Receiving user data form register form UI as a dictionary put it into the database
		!!! Neded to be followed by sending confirmarion email to the address set.
		"""

		if isEmailUsed(user_data["email"]):
			user_data["creation_status"] = "Email is already in use";
			return user_data;

		user_data["password"] = makeHash(user_data["password"]);
		user_data["date.creation"] = getTimeStamp();
		user_data["date.update"] = user_data["date.creation"];
		user_data["status"] = "Pending email confirmation";
		user_data["field.utility"] = makeHash(user_data["email"] + user_data["date.update"]);
		user_data["creation_status"] = "Ok";

		self.id = self.db.request("insert", user_data);

		user_data["id"] = self.id;

		return user_data;

	def login(self, user_data):
		"""
		checking credentials, return false if no match.
		user_data HAS to contain "email" field [used as login here]
		"""

		user_data["password"] = makeHash(user_data["password"]);

		if self.db.request("getOne", user_data):
			return True;
		else:
			return False;

	def loginState(self, user_data):
		"""
		checking credentials, return false if no match.
		if the user_data['password'] hash is stored in temporary cookie, no need to call hashinfg method each time.
		user_data HAS to contain "email" field [used as login here]
		"""
		if self.db.request("getOne", user_data):
			return True;
		else:
			return False;

	def confirmEmail(self, secret_hash):
		"""
		secret_hash is generated when creating user or updating user's email and sent to that email.
		This method checks secret_hash to be present in db
		"""

		the_data = {};
		the_data["field.utility"] = secret_hash;

		result = self.db.request("getOne", the_data);

		if result:
			data_prime = self.db.getData(result["_id"], {"status": "Ok"});

			result2 = self.db.request("update", data_prime);

			if result2:
				return "Ok";
			else:
				return False;

		else:
			return False;

	def updateUser(self, new_data): #new_data is a dict with new fields
		"""
		a method to update user data 
		"""

		the_data = {};
		the_data["email"] = self.email;
		
		new_data["date.update"] = getTimeStamp();

		data_prime = self.db.getData(the_data, new_data);

		result = self.db.request("update", data_prime);

		if result:
			return new_data;
		else:
			return False;

	def restoreRequest(self, email):
		"""
		a method to place a secret hash to the db to restore when user visits secret link.
		"""
		result = self.db.request("getOne", {"email": email});
		if result:
			new_data = {};
			new_data["field.utility"] = makeHash(email + getTimeStamp() + result["password"]);

			data_prime = self.db.getData(result["_id"], new_data);

			result2 = self.db.request("update", data_prime);

			if result2:
				return "Ok";
			else:
				return False;

		else:
			return False;

	def restorePassword(self, secret_hash, new_password):
		"""
		method to restore password after checking the secret.
		the call of restoreRequest earlier is presumed.
		"""

		result = self.db.request("getOne", {"field.utility": secret_hash});

		if result:
			new_data = {};
			new_data["password"] = makeHash(new_password);
			new_data["field.utility"] = "";

			data_prime = self.db.getData(result["_id"], new_data);

			result2 = self.db.request("update", data_prime);

			if result2:
				return "Ok";
			else:
				return False;

		else:
			return False;