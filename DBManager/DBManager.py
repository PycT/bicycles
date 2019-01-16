from pymongo import MongoClient;
import time;
import datetime;

class DBManager:

	def __init__(self, host = None, port = None):

		self.user = "System";
		if not host:
			self.client = MongoClient();
		else:
			db_uri = "mongodb://{}".format(host);
			if port:
				db_uri += ":{}".format(port);
			db_uri += "/";

			self.client = MongoClient(db_uri);

	def setDB(self, db_name = "default"):

		self.db = self.client[db_name];

	def setCollection(self, collection):

		self.collection = collection;

	def updateData(by_params, new_data): #parameters are dictionaries

		return [by_params, {"$set": new_data}];

	def logAction(self, operation, data, user = self.user):

		timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S');
		record = '\{"timestamp":{}, "user":{}, "operation":{}, "collection":{}, "data":{}\}'.format(timestamp, user, operation, self.collection, data);
		self.db.DBJournal.insert_one(record);
		pass;

	def request(self, operation, data, sort = None, log = False):

		if operation == "insert":

			result = self.collection.insert_one(data).inserted_id; #data is a dictionary

			if log:
				logAction(operation = "insert", data = data);

			return result;

		if operation == "insertBatch":

			result = self.collection.insert_many(data).inserted_ids; #batch is a list of dictionaries;

			if log:
				logAction(operation = "insert", data = data);

			return result;


		if operation == "getOne":

			return self.collection.find_one(data); #data is dictionary; use "_id" field to get by id.


		if operation == "get":

			if sort:
				return self.collection.find(data).sort(sort);
			else:
				return self.collection.find(data);


		if operation == "update": #!!! use updateData() method to form data param for update request.

			result = self.collection.updateMany(data[0], data[1]);

			if log:
				logAction(operation = "update", data = data);

			return result;

		if operation == "delete":

			result = self.collection.deleteMany(data);

			if log:
				logAction(operation = "delete", data = data);

			return result;


		

