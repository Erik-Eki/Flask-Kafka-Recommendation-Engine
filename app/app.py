from algo import get_recommendations
from flask import Flask, Response, render_template, request
from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer, KafkaConsumer
app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Recommendation page
@app.route('/recommend', methods=['POST'])
def recommend():
    # # Get the user's viewing history
    # history = request.form['history']

    # # Make recommendations based on the user's viewing history
    # recommendations = get_recommendations(history)
    # Get the user preferences from the form
    user_preferences = request.form
    
    # Call the recommendation system function to get the recommended movies
    recommendations = get_recommendations(user_preferences)

    # Render the recommendations page with the recommendations
    return render_template('recommend.html', recommendations=recommendations)


@app.route('/stream')
def stream():
    #127.0.0.1:9092
    consumer = KafkaConsumer('recommendations', bootstrap_servers=['kafka_b:9094'])
    def events():
        for msg in consumer:
            yield 'data: {0}\n\n'.format(msg.value)
    return Response(events(), mimetype="text/event-stream")

@app.route('/streaming')
def streaming():
    # Render the stream.html template and return it as a response
    return render_template('stream.html')

@app.route('/message', methods=['POST'])
def create_message():
    message = request.form.get('message').encode('ASCII')
    producer = KafkaProducer(bootstrap_servers=['kafka_b:9094'])
    producer.send('recommendations', message)
    return "Sent message to broker!"
    
@app.route('/message')
def message():
    return render_template('create_message.html')






@app.route('/create_topic', methods=['POST'])
def create_topic():
    # Get the topic name from the user input
    topic_name = request.form.get('topic_name')

    # Create a KafkaAdminClient object
    admin_client = KafkaAdminClient(bootstrap_servers='kafka_b:9094')

    # Create a NewTopic object
    new_topic = NewTopic(name=topic_name, num_partitions=1, replication_factor=1)

    # Call the create_topics method to create the topic
    admin_client.create_topics(new_topics=[new_topic])

    # Return a success message
    return f'Topic {topic_name} created successfully'

@app.route('/create_topic')
def topic():
    return render_template('create_topic.html')


if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    # app.run(debug=True, host='0.0.0.0', port=port)
    app.run(debug=True)
