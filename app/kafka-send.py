from kafka import KafkaProducer
import json

# Create a Kafka producer
# producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
producer2 = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

message = b'Hello, from Python, in variable, without fluff!'

producer.send('recommendations', message)
producer2.send('recommendations', {'message': 'Hello, from Python, JSON!'})

print("Sent message: ", message)