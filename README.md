### What is This?
A simple PoC on Kafka broker (containerized), producer (containerized), consumer (on host machine) setup, communication etc.

### Setup/Testing

The following steps are for scripts located in `./1-with-docker` folder -

1. Create a docker network so that producer container can communicate with broker container using broker's container name -
```
docker network create test_network
```

2. start kafka-broker docker container in `test_network` using -
```
cd broker
docker-compose up -d
```

3. Ensure broker has started by checking container logs -
```
docker logs kafka-broker
```

4. Start kafka-producer docker container in `test_network` -
```
cd ../producer
bash build_image.sh
bash run_container.sh
```

5. Ensure producer sent a message -
```
docker logs kafka-producer-c
```

6. Check if consumer on host can retrieve producer's message -
```
cd ../consumer
python consumer.py
```

Refer `README.md` present in `2-without-docker` for steps without docker
