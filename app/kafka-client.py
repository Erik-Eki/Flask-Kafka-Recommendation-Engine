# Import the kafka-python package
from kafka import KafkaProducer, KafkaConsumer
# Import the recommend_movies function from the Flask app
from algo import get_recommendations
# Import the json package
import json

# Create a Kafka producer
# producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
# producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])

# Create a Kafka consumer
# consumer = KafkaConsumer(bootstrap_servers=['127.0.0.1:9092'], group_id='recommendation-group', value_deserializer=lambda v: json.loads(v.decode('utf-8')))
consumer = KafkaConsumer('recommendations', bootstrap_servers=['127.0.0.1:9092'])


# producer.send('test', b'Ebin!')
# consumer.poll(timeout_ms=1000)

# Subscribe to the topics
# consumer.subscribe(['preferences', 'recommendations'])
consumer.subscribe('recommendations')

print("Listening for messages...")

for msg in consumer:
    print(msg.value)
# Loop over the messages from the consumer
# for msg in consumer:
    
#     # Get the topic, key, and value of the message
#     topic = msg.topic
#     key = msg.key
#     value = msg.value

#     # If the topic is preferences, get the recommendations and send them to the recommendations topic
#     if topic == 'preferences':
#         # Get the preferences from the value
#         preferences = value['preferences']

#         # Call the recommend_movies function to get the recommendations
#         recommendations = get_recommendations(preferences)

#         # Send the recommendations to the recommendations topic
#         producer.send('recommendations', key=key, value={'recommendations': recommendations})

#     # If the topic is recommendations, print the recommendations to the console
#     elif topic == 'recommendations':
#         # Get the recommendations from the value
#         recommendations = value['recommendations']

#         # Print the recommendations to the console
#         print(f'Recommendations for user {key}: {recommendations}')
