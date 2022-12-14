from constants import *

import json

from kafka import KafkaProducer

CLIENT_ID = 'client-producer-1'

def producer():

    print('producer: sending message(s)...')
    producer = KafkaProducer(
        bootstrap_servers=BROKER_LIST,
        client_id=CLIENT_ID
    )

    message = {
        'country': 'India-8',
        'capital': 'Delhi'
    }
    producer.send(
        TOPIC_NAME, 
        json.dumps(message).encode()
    )
    print('producer: initiated send request')

if __name__ == '__main__':
    producer()