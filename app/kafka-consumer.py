from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('vidya',
                        #  bootstrap_servers=['localhost:9092'],
                        bootstrap_servers=['kafka:9092'],
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    print(message.value)