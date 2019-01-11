from pymongo import MongoClient;

class DBManager:

	def __init__(self, host = None, port = None):

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


	def request(self, operation, data, sort = None):

		if operation == "insert":

			return self.collection.insert_one(data).inserted_id; #data is a dictionary

		if operation == "insertBatch":

			return self.collection.insert_many(data).inserted_ids; #batch is a list of dictionaries;

		if operation == "getOne":

			return self.collection.find_one(data); #data is dictionary; use "_id" field to get by id.

		if operation == "get":

			if sort:
				return self.collection.find(data).sort(sort);
			else:
				return self.collection.find(data);

		if operation == "update": #!!! use updateData method to form data param for update request.

			return self.collection.updateMany(data[0], data[1]);

		if operation == "delete":

			return self.collection.deleteMany(data);


		

