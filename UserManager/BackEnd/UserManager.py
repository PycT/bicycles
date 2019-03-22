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
"status" field is also used to confirm email.
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
		user_data["status"] = makeHash(getTimeStamp() + user_data["password"] + user_data["email"]);
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

	def confirmEmail(self, secret_hash):
		"""
		secret_hash is generated when creating user or updating user's email and sent to that email.
		This method checks secret_hash to be present in db
		"""

		the_data = {};
		the_data["status"] = secret_hash;

		result = self.db.request("getOne", the_data);

		if result:
			data_prime = self.db.getData(the_data, "Ok");

			result2 = self.db.request("update", data_prime);

			if result2:
				return "Ok";
			else:
				return False;

		else:
			return False;

