import grpc;
import HMAlerts_pb2;
import HMAlerts_pb2_grpc;
import time;


#every method logs the update agent, if specified in hm_agent argument
# possible arguments:
# 	hm_alert_id - the id, genberated when alert is created via setAlert()
#	hm_agent - agent performing an action over an alert
#	hm_status - 'Red' for active, 'Yellow' for suspended, 'Green' for dismissed
#	hm_message - the text message of an alert
#	hm_suspend_for - time in seconds to suspend (integer)
#
# fields of alerts:
#	Created - timestamp of the alert creation
#	Updated - timestamp of the alert update
#	Suspended - time in seconds the alert suspended for
#	Alert Message - alert message
#	Last Action - the action performed last on the alert
#	Last Agent - who did perform the last action over the alert

def run():

	channel = grpc.insecure_channel('alertmanager:8001');
	stub = HMAlerts_pb2_grpc.AlertManagerStub(channel);

	response = stub.setAlert(HMAlerts_pb2.hmAlert(hm_message = 'Test Alert 1')); #Setting an alert returns a new alert's id
	the_id = response.content; #getting the new alert id
	print(the_id);

	stub.setAlert(HMAlerts_pb2.hmAlert(hm_message = 'Test Alert 2'));
	stub.setAlert(HMAlerts_pb2.hmAlert(hm_agent='ZZ Top', hm_message = 'Test Alert 3'));
	stub.setAlert(HMAlerts_pb2.hmAlert(hm_message = 'Test Alert 4'));
	stub.setAlert(HMAlerts_pb2.hmAlert(hm_message = 'Test Alert 5'));
	stub.setAlert(HMAlerts_pb2.hmAlert(hm_message = 'Test Alert 6'));

	stub.suspendAlert(HMAlerts_pb2.hmAlert(hm_suspend_for = 1300));#hm_suspend_for is optional, default is 300;
	#stub.suspendAlert(HMAlerts_pb2.hmAlert(hm_alert_id = the_id));#suspend is available by id or in bulk only.

	stub.unsuspendAlert(HMAlerts_pb2.hmAlert(hm_alert_id = the_id));#unsuspend is available by id or in bulk only. 
	

	stub.dismissAlert(HMAlerts_pb2.hmAlert());#dismiss is available by id or in bulk only.


	stub.reactivateAlert(HMAlerts_pb2.hmAlert(hm_alert_id = the_id, hm_agent = 'F. Mulder'));#reactivate is available by id or in bulk only.

	print();
	#result = stub.getAlert(HMAlerts_pb2.hmAlert(hm_message = 'Test Alert 5')).content; #Alert might be gotten by id, messsage, status or agent (or combination of the fields)
	result = stub.getAlert(HMAlerts_pb2.hmAlert()).content; #Getting all alerts
	print(result); 

	print('-----Suspend controller test-----');

	print(stub.getAlert(HMAlerts_pb2.hmAlert(hm_alert_id = the_id)).content);

	time.sleep(0.5);

	print('Suspending');
	print(stub.suspendAlert(HMAlerts_pb2.hmAlert(hm_alert_id = the_id, hm_suspend_for = 10)).content);
	print(stub.getAlert(HMAlerts_pb2.hmAlert(hm_alert_id = the_id)).content);

	print('Pause 21 seconds'); #suspend controller in our HMAlertService invoked every 10 seconds.
	time.sleep(21);
	print(stub.getAlert(HMAlerts_pb2.hmAlert(hm_alert_id = the_id)).content);

if __name__ == '__main__':
	run();