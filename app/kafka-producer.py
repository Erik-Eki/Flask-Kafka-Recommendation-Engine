from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                        # bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))

with open('./data/video_game_data.csv') as f:
    next(f) # Skip the header row
    for line in f:
        producer.send('vidya', line)
        time.sleep(0.1) # Add a delay to simulate streaming