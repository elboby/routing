# coding=utf-8            
from tasks import RoutingTask


relay_methods = ['method1', 'method2']
order = {'id': 1,
	     'message': {'type': 'bla', 'message': '#1'},
         'status': 'NEW'}


if __name__ == "__main__":
    routing_task = RoutingTask(order, relay_methods)
    routing_task.route()
