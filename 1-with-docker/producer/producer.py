import json

from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

CLIENT_ID = 'client-producer-1'
TOPIC_NAME = 'topic-test1'
BROKER_LIST = ['kafka-broker:29092']

def create_topic(topic_name):

    admin_client = KafkaAdminClient(
        bootstrap_servers=BROKER_LIST, 
        client_id=CLIENT_ID
    )

    topics_present = admin_client.list_topics()
    if topic_name in topics_present:
        print(f'{topic_name} already present.')
        return

    print(f'creating {topic_name}...')
    topic_list = []
    
    topic_list.append(
        NewTopic(
            name=topic_name, 
            num_partitions=1, 
            replication_factor=1
        )
    )
    
    admin_client.create_topics(
        new_topics=topic_list, 
        validate_only=False
    )
    print('intiated creation')
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
    future = producer.send(
        TOPIC_NAME, 
        json.dumps(message).encode()
    )
    res = future.get()
    print(f"message with offset={res.offset} sent")

if __name__ == '__main__':
    create_topic(TOPIC_NAME)
    producer()