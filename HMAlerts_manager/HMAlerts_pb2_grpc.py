# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import HMAlerts_pb2 as HMAlerts__pb2


class AlertManagerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.setAlert = channel.unary_unary(
        '/AlertManager/setAlert',
        request_serializer=HMAlerts__pb2.hmAlert.SerializeToString,
        response_deserializer=HMAlerts__pb2.hmResponse.FromString,
        )
    self.suspendAlert = channel.unary_unary(
        '/AlertManager/suspendAlert',
        request_serializer=HMAlerts__pb2.hmAlert.SerializeToString,
        response_deserializer=HMAlerts__pb2.hmResponse.FromString,
        )
    self.unsuspendAlert = channel.unary_unary(
        '/AlertManager/unsuspendAlert',
        request_serializer=HMAlerts__pb2.hmAlert.SerializeToString,
        response_deserializer=HMAlerts__pb2.hmResponse.FromString,
        )
    self.dismissAlert = channel.unary_unary(
        '/AlertManager/dismissAlert',
        request_serializer=HMAlerts__pb2.hmAlert.SerializeToString,
        response_deserializer=HMAlerts__pb2.hmResponse.FromString,
        )
    self.reactivateAlert = channel.unary_unary(
        '/AlertManager/reactivateAlert',
        request_serializer=HMAlerts__pb2.hmAlert.SerializeToString,
        response_deserializer=HMAlerts__pb2.hmResponse.FromString,
        )
    self.getAlert = channel.unary_unary(
        '/AlertManager/getAlert',
        request_serializer=HMAlerts__pb2.hmAlert.SerializeToString,
        response_deserializer=HMAlerts__pb2.hmResponse.FromString,
        )


class AlertManagerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def setAlert(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def suspendAlert(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def unsuspendAlert(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def dismissAlert(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def reactivateAlert(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getAlert(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AlertManagerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'setAlert': grpc.unary_unary_rpc_method_handler(
          servicer.setAlert,
          request_deserializer=HMAlerts__pb2.hmAlert.FromString,
          response_serializer=HMAlerts__pb2.hmResponse.SerializeToString,
      ),
      'suspendAlert': grpc.unary_unary_rpc_method_handler(
          servicer.suspendAlert,
          request_deserializer=HMAlerts__pb2.hmAlert.FromString,
          response_serializer=HMAlerts__pb2.hmResponse.SerializeToString,
      ),
      'unsuspendAlert': grpc.unary_unary_rpc_method_handler(
          servicer.unsuspendAlert,
          request_deserializer=HMAlerts__pb2.hmAlert.FromString,
          response_serializer=HMAlerts__pb2.hmResponse.SerializeToString,
      ),
      'dismissAlert': grpc.unary_unary_rpc_method_handler(
          servicer.dismissAlert,
          request_deserializer=HMAlerts__pb2.hmAlert.FromString,
          response_serializer=HMAlerts__pb2.hmResponse.SerializeToString,
      ),
      'reactivateAlert': grpc.unary_unary_rpc_method_handler(
          servicer.reactivateAlert,
          request_deserializer=HMAlerts__pb2.hmAlert.FromString,
          response_serializer=HMAlerts__pb2.hmResponse.SerializeToString,
      ),
      'getAlert': grpc.unary_unary_rpc_method_handler(
          servicer.getAlert,
          request_deserializer=HMAlerts__pb2.hmAlert.FromString,
          response_serializer=HMAlerts__pb2.hmResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'AlertManager', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
