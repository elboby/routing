# coding=utf-8
import json

import gateways


class TransactionTask(object):

    def __init__(self, order, gateway):
        self.order = order
        self.gateway = gateway
        
    def run(self):
        message_json = self.transform_order_to_json(self.order)
        self.gateway.publish(message_json)

    @classmethod
    def transform_order_to_json(self, order):
        return json.dumps(order['message'])

class RoutingTask(object):
    
    def __init__(self, order, relay_methods, *args, **kwargs):
        self.order = order
        self.relay_methods = relay_methods
    
    def route(self):
        if not self.relay_methods:
            self.order['status'] = 'ERROR'
            print self.order['status']
            print 'The End.'
            return

        current_relay_method = self.relay_methods.pop(0)
        t = TransactionTask(self.order, gateways.GATEWAYS[current_relay_method])
        t.run()
