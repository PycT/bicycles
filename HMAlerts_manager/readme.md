A microservice to manage alerts

Essential settings
	
	in HMAlertService.py:
		- mongoDB settings in the constructor of HMAService class (lines near 25th)
		- gRPC channel settings in the serve() function, 'server.add_insecure_port('[::]:8001');', line 61

	client side (e.g. in HMAlerts_client.py):
		- client-side gRPC channel setting - 'channel = grpc.insecure_channel('alertmanager:8001');', line 14


See the HMAlerts_client.py to get how this microservice works.

HMAlerts.py - the core class.