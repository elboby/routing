# coding=utf-8
from pika_utils import get_pika_connection, get_channel, publish_message


def callback(channel, method, properties, message):
    print 'Message from service:', message
    response = {'status': 'OK',
                'order': message} 

if __name__ == "__main__":
    pkcon = get_pika_connection()
    channel = get_channel(pkcon, 'helicom_test_queue_from_service')
    channel.basic_consume(callback, no_ack=True)

    print 'starting consumption of messages from service'
    channel.start_consuming()
