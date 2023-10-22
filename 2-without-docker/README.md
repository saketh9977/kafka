### What is this?
A small demo on kafka consumer & producer in Python -
1. Orchestrator 
    - Delete a topic
    - Create a topic
    - Retrieve all topics
2. Producer
    - Send a message to a topic
5. Consumer
    - Subscribe to a topic
    - Retrieve messages from a topic; uses group_id to maintain offset for each consumer.

### Pre-requisites
1. Java
2. Python

### How to Run?
1. Download Kafka from [here](https://kafka.apache.org/quickstart)
2. Start zookeeper & server (broker)
3. Install python dependencies using `pip install -r requirements.txt`
4. Create kafka topic using `cd src` & `python orchestrator.py`
5. Start producer using `python producer.py`
6. Start consumer using `python consumer.py`