from constants import *

import json

from kafka import KafkaConsumer

CLIENT_ID = 'client-consumer-1'
GROUP_ID = 'group-consumer-1'

def consumer():

    """
        1. group_id is used by kafka to determine offset for a consumer -
        i.e. which message to send to a given consumer. Using group_id -
        a consumer can retrieve all past "unretrieved messages".
    """

    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=BROKER_LIST,
        client_id=CLIENT_ID,
        group_id=GROUP_ID,
        consumer_timeout_ms=1000
    )

    print('fetching messages...')
    for message in consumer:
        print(json.loads(message.value))
    print('exiting...')

def subscribe_to_topic(topic_name):

    print(f'subscribing to topic {topic_name}...')
    consumer = KafkaConsumer(
        bootstrap_servers=BROKER_LIST,
        client_id=CLIENT_ID
    )

    consumer.subscribe(topic_name)
    print('subscription request initiated')

if __name__ == '__main__':
    subscribe_to_topic(TOPIC_NAME)
    consumer()