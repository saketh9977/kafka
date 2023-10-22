from constants import *

from kafka.admin import KafkaAdminClient, NewTopic

CLIENT_ID = 'client-orchestrator'

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

def delete_topic(topic_name):

    admin_client = KafkaAdminClient(
        bootstrap_servers=BROKER_LIST, 
        client_id=CLIENT_ID
    )

    topics_present = admin_client.list_topics()
    if (topic_name in topics_present) == False:
        print(f'{topic_name} is absent.')
        return
    
    print(f'deleting {topic_name}...')
    admin_client.delete_topics([topic_name])
    print('initiated deletion')

def orchestrator():
    create_topic(TOPIC_NAME)
    # delete_topic(TOPIC_NAME)

if __name__ == '__main__':
    orchestrator()
