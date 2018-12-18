from pymongo import MongoClient;
from concurrent import futures;

import grpc;
import time;

import HMAlerts;
import HMAlerts_pb2_grpc;
import HMAlerts_pb2;



class HMAService(HMAlerts_pb2_grpc.AlertManagerServicer):

	def __init__(self):

		hm_db_client = MongoClient('mongodb', 27017);
		hm_db = hm_db_client.HMAlertsDb;
		hm_collection = hm_db.HMAlertsCollection;

		self.hm_alerts_manager = HMAlerts.HMAlerts(hm_collection);


	def setAlert(self, request, context):

		return HMAlerts_pb2.hmResponse(content = self.hm_alerts_manager.setAlert(hm_message = request.hm_message, hm_agent = request.hm_agent, hm_status = request.hm_status));

	def suspendAlert(self, request, context):

		return HMAlerts_pb2.hmResponse(content = self.hm_alerts_manager.suspendAlert(hm_alert_id = request.hm_alert_id, hm_suspend_for = request.hm_suspend_for, hm_agent = request.hm_agent));

	def unsuspendAlert(self, request, context):

		return HMAlerts_pb2.hmResponse(content = self.hm_alerts_manager.unsuspendAlert(hm_alert_id = request.hm_alert_id, hm_agent = request.hm_agent));

	def dismissAlert(self, request, context):

		return HMAlerts_pb2.hmResponse(content = self.hm_alerts_manager.dismissAlert(hm_alert_id = request.hm_alert_id, hm_agent = request.hm_agent));

	def reactivateAlert(self, request, context):

		return HMAlerts_pb2.hmResponse(content = self.hm_alerts_manager.reactivateAlert(hm_alert_id = request.hm_alert_id, hm_agent = request.hm_agent));

	def getAlert(self, request, context):

		return HMAlerts_pb2.hmResponse(content = self.hm_alerts_manager.getAlert(hm_alert_id = request.hm_alert_id, hm_message = request.hm_message, hm_agent = request.hm_agent, hm_status = request.hm_status));

	def checkSuspends(self):
		
		return self.hm_alerts_manager.checkSuspends();

def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10));
	hm_alerts_instance = HMAService();
	HMAlerts_pb2_grpc.add_AlertManagerServicer_to_server(hm_alerts_instance, server);
	server.add_insecure_port('[::]:8001');
	server.start()

	try:
		while True:
			time.sleep(10);
			hm_alerts_instance.checkSuspends()
	except KeyboardInterrupt:
		print();
		server.stop(0);


if __name__ == '__main__':
	print('Starting the server, press ^C to stop.')
	serve();
