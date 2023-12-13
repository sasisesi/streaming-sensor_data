import datetime
import random
import json
import time
import os
from google.cloud import pubsub_v1

# Set your Google Cloud project and topic information
project_id = 'PROJECT-ID'
topic_id = 'TOPIC-ID'

# Set the path to your uploaded Google Cloud service account key file
keyfile_path = 'SERVICE ACCOUNT JSON FILE PATH'  # Update this with the correct path

# Set the environment variable for Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = keyfile_path

# Create a Publisher client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Simulate data generation and publishing for one day
def generate_sensor_data():
    while True:
        timestamp = datetime.datetime.utcnow()

        temperature = round(random.uniform(20, 30), 2)
        humidity = round(random.uniform(30, 70), 2)
        water_leakage = random.choice([True, False])
        motion_detected = random.choice([True, False])

        sensor_data = {
            "timestamp": timestamp.isoformat(),
            "temperature": temperature,
            "humidity": humidity,
            "water_leakage": water_leakage,
            "motion_detected": motion_detected
        }

        # Convert the dictionary to JSON format
        json_message = json.dumps(sensor_data)

        # Publish the message to the Pub/Sub topic
        future = publisher.publish(topic_path, data=json_message.encode('utf-8'))

        print(sensor_data)

        # Sleep for one second
        time.sleep(1)

if __name__ == '__main__':
    try:
        generate_sensor_data()
    except KeyboardInterrupt:
        print("Data generation stopped.")