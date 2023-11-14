# Flask-Kafka-Recommendation-engine

![image](https://github.com/Erik-Eki/Flask-Kafka-Recommendation-Engine/assets/70281449/b09878d2-f551-4a07-98b3-9061f1931bf5)

 A small project for learning Kafka. You can pick a genre and mininum rating to get 10 video game recommendations. You can also send and listen to Kafka messages.

 Using:
 - Flask server (Python)
 - Kafka
 - Provectuslabs Kafka UI

# Endpoints

**Get video game recommendations**
`http://localhost:5000/`

**Send message to "recommendations" Kafka-topic**
`http://localhost:5000/message`

**Listen from message on "recommendations" Kafka-topic**
`http://localhost:5000/streaming`

---

# Docker setup & Usage

First, build:
`docker-compose build`

Then, you can take the stack down and put it up.
`docker-compose down --remove-orphans && docker-compose -p kafka-service up -d`

Creates a docker-stack named "kafka-service". To get into the Kafka container, it's going to be named something like this:

```bash
$ docker exec -it kafka-service-kafka_b-1 /bin/bash
```

---

Inside Kafka container, you can now access Kafka's controls:

**Listing topics:**
```bash
$ kafka-topics.sh --list  --bootstrap-server kafka_b:9092
```

**Creating topics**
```bash
$ kafka-topics.sh --create --topic recommendations --partitions 4 --replication-factor 1  --bootstrap-server kafka_b:9092`
```

**Describing topics**
```bash
$ kafka-topics.sh --describe --topic recommendations --bootstrap-server kafka_b:9092
```

**Insert (Produce) a topic**
```bash
$ kafka-console-producer.sh --topic=recommendations --broker-list=kafka_b:9092
>Hello World!
>This is text!
```

**Read (Consume) a topic**
```bash
$ kafka-console-consumer.sh --topic=recommendations --from-beginning  --bootstrap-server kafka_b:9092
```
