import os
from google.cloud import pubsub_v1
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email(message_data, context=None):
    # Replace with your SendGrid API key
    sendgrid_api_key = 'SENDGRID API KEY'
    sender_email = 'SENDER EMAIL'
    recipient_email = 'RECIVER EMAIL'

    # Set up SendGrid client
    sg = SendGridAPIClient(sendgrid_api_key)

    # Create SendGrid email
    email_message = Mail(
        from_email=sender_email,
        to_emails=recipient_email,
        subject='Pub/Sub Notification',
        plain_text_content=f'Message received: {message_data}'
    )

    # Send the email
    response = sg.send(email_message)

    return response

def pubsub_trigger(data, context):
    # Decode the Pub/Sub message data
    message_data = data['data'].decode('utf-8')
    
    # Send an email using SendGrid
    response = send_email(message_data, context)

    # Log the SendGrid response
    print(f"SendGrid response: {response.status_code}")

# Test the send_email function
# Uncomment the following lines and replace placeholders with real values to test the email sending
# test_message_data = "Test message data"
# test_response = send_email(test_message_data)
# print(f"Test SendGrid response: {test_response.status_code}")