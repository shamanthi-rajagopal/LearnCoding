import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main():
    # Prompt the user to input the variable
    variable = input("Enter the variable: ")

    connect(variable)


def connect(variable):
    
    send_email(variable)

def send_email(variable):
    # Construct the email message with the provided variable
    message = Mail(
        from_email='shamanthi2025@gmail.com',
        to_emails='shamanthi2025@gmail.com',
        subject='Sending with Twilio SendGrid: Variable Value',
        html_content=f'<strong> Hello, this email is sent to tell you that the variable value is: {variable}</strong>')

    # Initialize the SendGrid client with your API key
    sg = SendGridAPIClient('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')

    # Send the email
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)

main()  # program starts here
