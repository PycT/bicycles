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

	def getTimeStamp():

		return datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S");

	def isEmailUsed(self, email):

		testq = {"email": email};
		test_result = self.db.request("getOne", testq);

		if test_result:
			return True;
		else:
			return False;

	def create(self, user_data): #user_data is a dictionary

		if isEmailUsed(user_data["email"]):
			return "Email is already in use";

		user_data["password"] = makeHash(user_data["password"]);
		user_data["date.creation"] = getTimeStamp();
		user_data["date.update"] = user_data["date.creation"];
		user_data["status"] = "pending";
		user_data["field.utility"] = makeHash(user_data["email"] + user_data["date.update"]);

		self.id = self.db.request("insert", user_data);

		return "Ok";

	def login(self, user_data):

		user_data["password"] = makeHash(user_data["password"]);

		if self.db.request("getOne", user_data):
			return True;
		else:
			return False;
