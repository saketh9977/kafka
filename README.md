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