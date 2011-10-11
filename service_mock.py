# coding=utf-8
from pika_utils import get_pika_connection, get_channel, publish_message


def callback(channel, method, properties, message):
    print 'Message from gateway:', message
    response = {'status': 'OK',
                'order': message} 
    print 'Sending a response: ', response
    publish_message(message, channel, 'helicom_test_queue_from_service')	


if __name__ == "__main__":
    pkcon = get_pika_connection()
    channel = get_channel(pkcon, 'helicom_test_queue_from_gateway')
    channel.basic_consume(callback, no_ack=True)

    print 'starting consumption of messages from gateway'
    channel.start_consuming()
