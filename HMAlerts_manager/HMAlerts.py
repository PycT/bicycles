import time;
from pymongo import MongoClient;
from bson.objectid import ObjectId;

class HMAlerts:

	class AlertException(Exception):
		def __init__(self, value):
			self.value = value;
		def ___str___(self):
			return repr(self.value);


	def __init__(self, hm_collection = None): 

		self.message = "None";
		self.operationStatus = " ok ";
		self.suspendTime = 0;
		self.time_stamp = time.time();
		self.status = "Green";

		
		if not hm_collection: 
			raise AlertException("Fatal: database collection undefined. Can't continue, sorry.");
			exit();
		else:
			self.alarms_collection = hm_collection;

	def setAlert(self, hm_message = "Alert!", hm_agent = "Default", hm_status = "Red"):
		'''create alert'''

		self.time_stamp = time.time();

		if hm_message == '':
			hm_message = 'Alert!';

		if hm_agent == '':
			hm_agent = 'Default';

		if hm_status == '':
			hm_status = 'Red';

		hm_alert_record = {"Created": self.time_stamp, "Updated": self.time_stamp, "Alert Message": hm_message, "Status": hm_status, "Suspended": 0, "Last Action": "Created", "Last Agent": hm_agent};
		try:
			recordId = self.alarms_collection.insert_one(hm_alert_record).inserted_id;
		except Exception as e:
			self.status=repr(e);
			return str(self.status);

		self.operationStatus = "success";
		return str(recordId);

	def suspendAlert(self, hm_alert_id = None, hm_suspend_for = 300, hm_agent = "Default"):
		''' if id not set suspend all unsuspended alarms ''';

		self.time_stamp = time.time();

		if hm_suspend_for == 0:
			hm_suspend_for = 300;

		if hm_agent == '':
			hm_agent = 'Default';

		if not hm_alert_id:
			try:
				self.alarms_collection.update_many({"Suspended": 0}, {"$set":{"Suspended":hm_suspend_for, "Status":"Yellow", "Last Action":"Suspended (in bulk)", "Last Agent":hm_agent, "Updated":self.time_stamp}});
			except Exception as e:
				self.status = repr(e);
				return str(self.status);
			self.status = "success";
			return 'Success';
		else:
			try:
				suspended = self.alarms_collection.update_one({"_id": ObjectId(hm_alert_id)}, {"$set":{"Suspended":hm_suspend_for, "Status":"Yellow", "Last Action":"Suspended", "Last Agent":hm_agent, "Updated":self.time_stamp}});
			except Exception as e:
				self.status = repr(e);
				return str(self.status);
			if suspended.modified_count > 0:
				self.status = "success";
				return 'Success';
			else:
				self.status = 'nothing modified';
				return 'Nothing Suspended (incorrect AlertId?)';

	def unsuspendAlert(self, hm_alert_id = None, hm_agent = "Default"):
		''' if id not set unsuspend all suspended alarms ''';

		self.time_stamp = time.time();

		if hm_agent == '':
			hm_agent = 'Default';

		if not hm_alert_id:
			try:
				self.alarms_collection.update_many({"Suspended": {"$ne":0}}, {"$set":{"Suspended":0, "Status":"Red", "Last Action":"Unsuspended (in bulk)", "Last Agent":hm_agent, "Updated":self.time_stamp}});
			except Exception as e:
				self.status = repr(e);
				return str(self.status);
			self.status = "success";
			return 'Success';
		else:
			try:
				unsuspended = self.alarms_collection.update_one({"_id": ObjectId(hm_alert_id)}, {"$set":{"Suspended":0, "Status":"Red", "Last Action":"Unsuspended", "Last Agent":hm_agent, "Updated":self.time_stamp}});
			except Exception as e:
				self.status = repr(e);
				return str(self.status);
			if unsuspended.modified_count > 0:
				self.status = "success";
				return 'Success';
			else:
				self.status = 'nothing modified';
				return 'Nothing Unsuspended (incorrect AlertId?)';

	def dismissAlert(self, hm_alert_id = None, hm_agent = "Default"):
		''' if id not set dismiss all alarms ''';

		self.time_stamp = time.time();

		if hm_agent == '':
			hm_agent = 'Default';

		if not hm_alert_id:
			try:
				self.alarms_collection.update_many({"Status": {"$ne":"Green"}}, {"$set":{"Status":"Green", "Last Agent":hm_agent, "Last Action":"Dismissed (in bulk)", "Updated":self.time_stamp}});
			except Exception as e:
				self.status = repr(e);
				return str(self.status);
			self.status = "success";
			return 'Success';
		else:
			try:
				dismissed = self.alarms_collection.update_one({"_id": ObjectId(hm_alert_id)}, {"$set":{"Status":"Green", "Last Agent":hm_agent, "Last Action":"Dismissed", "Updated":self.time_stamp}});
			except Exception as e:
				self.status = repr(e);
				return str(self.status);
			if dismissed.modified_count > 0:
				self.status = "success";
				return 'Success';
			else:
				self.status = 'nothing modified';
				return 'Nothing Dismissed (incorrect AlertId?)';

	def reactivateAlert(self, hm_alert_id = None, hm_agent = "Default"):
		''' if id not set reactivate all alarms ''';

		self.time_stamp = time.time();

		if hm_agent == '':
			hm_agent = 'Default';

		if not hm_alert_id:
			try:
				self.alarms_collection.update_many({"Status": {"$ne":"Red"}}, {"$set":{"Status":"Red", "Last Agent":hm_agent, "Last Action":"Reactivated (in bulk)", "Updated":self.time_stamp}});
			except Exception as e:
				self.status = repr(e);
				return str(self.status);
			self.status = "success";
			return 'Success';
		else:
			try:
				reactivated = self.alarms_collection.update_one({"_id": ObjectId(hm_alert_id)}, {"$set":{"Status":"Red", "Last Agent":hm_agent, "Last Action":"Reactivated", "Updated":self.time_stamp}});
			except Exception as e:
				self.status = repr(e);
				return str(self.status);
			if reactivated.modified_count > 0:
				self.status = "success";
				return 'Success';
			else:
				self.status = 'nothing modified';
				return 'Nothing Reactivated (incorrect AlertId?)';

	def getAlert(self, **kwargs): #have to add orderby and select by time
		
		kwargs_verify = False;
	
		try:
			if ('hm_alert_id' in kwargs) and kwargs['hm_alert_id']:
				if kwargs['hm_alert_id']:
					alert_cursor = self.alarms_collection.find({'_id':ObjectId(kwargs['hm_alert_id'])});
					kwargs_verify = True;

			if ('hm_agent' in kwargs) and kwargs['hm_agent']:
				if kwargs['hm_agent']:
					alert_cursor = self.alarms_collection.find({'Last Agent':kwargs['hm_agent']}).sort('Updated', -1);
					kwargs_verify = True;

			if ('hm_message' in kwargs) and kwargs['hm_message']:
				if kwargs['hm_message']:
					alert_cursor = self.alarms_collection.find({'Alert Message': kwargs['hm_message']}).sort('Updated', -1);
					kwargs_verify = True;

			if ('hm_status' in kwargs) and kwargs['hm_status']:
				if kwargs['hm_status']:
					alert_cursor = self.alarms_collection.find({'Status': kwargs['hm_status']}).sort('Updated', -1);
					kwargs_verify = True;

			if not kwargs_verify:
				alert_cursor = self.alarms_collection.find();


			if alert_cursor.count() > 0:
				self.status = 'success';
				results = [];
				for record in alert_cursor:
					results.append(str(record));
				return '{\n'+',\n'.join(results)+'\n}';
			else:
				self.status = '- Nothing found -';
				return '- Nothing Found -';

		except Exception as e:

			self.status = repr(e);
			return str(self.status);

	def checkSuspends(self):

		self.time_stamp = time.time();

		try:
			alert_cursor = self.alarms_collection.find({'Status':'Yellow'});

			for record in alert_cursor:
				if self.time_stamp - record['Updated'] >= record['Suspended']:
					self.alarms_collection.update_one({"_id": record['_id']}, {"$set":{"Status":"Red", "Suspended":0, "Last Agent":"AlertManager Suspend Controller", "Last Action":"Unsuspended", "Updated":self.time_stamp}});

		except Exception as e:
			self.status = e;
			return str(e);

		return True;
