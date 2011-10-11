# coding=utf-8
import pika_utils


class BoxGateway(object):
    
    def __init__(self):
        self.connection = pika_utils.get_pika_connection()
        self.queue = 'helicom_test_queue_from_gateway'
        self.channel = pika_utils.get_channel(self.connection, self.queue)
        self.routing_key = 'helicom_test_queue_from_gateway'
    
    def publish(self, message):
        print "Publishing to service:", message 
        pika_utils.publish_message(message, self.channel, self.routing_key)
    
GATEWAYS = {'method1': BoxGateway(),
            'method2': None}
