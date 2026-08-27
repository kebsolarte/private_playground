import os
from dotenv import load_dotenv
import pandas as pd
import smtplib as smtp
from email.message import EmailMessage
import datetime as dt
import random

# Initialize .env variables
load_dotenv()


# Get email credentials
sender_email = os.getenv("WORK_GMAIL_UN")
sender_email_pw = os.getenv("WORK_GMAIL_APP_PW")


# Load email templates paths into a list
templates_paths = ["./letter_templates/letter_1.txt", 
                   "./letter_templates/letter_2.txt", 
                   "./letter_templates/letter_3.txt"]


# Load birthdays.csv into a DF object
birthdays = pd.read_csv('birthdays.csv')


# Create basic functions
def check_birthday(file: pd.DataFrame) -> dict:
    """Checks birthdays list and returns a dict containing the name and email of the celebrant"""
    # Checks if there is a matching birthdate today
    for _, row in file.iterrows():
        if row['month'] == dt.datetime.now().month and row['day'] == dt.datetime.now().day:
            return {'name': row['name'], 'email': row['email']}
    return None


def construct_greeting(templates:list, celebrant:dict) -> EmailMessage:
    """Constructs the email message object from the templates and celebrant details"""
    # Load a random template and replace name placeholder
    with open(random.choice(templates), mode='r') as template:
        greeting_msg = template.read()
        greeting_msg = greeting_msg.replace('[NAME]', celebrant['name'])

    # Construct the email message object
    email_msg = EmailMessage()
    email_msg['From'] = sender_email
    email_msg['To'] = celebrant['email']
    email_msg['Subject'] = f"Happy Birthday, {celebrant['name']}!"
    email_msg.set_content(greeting_msg)

    return email_msg


def send_greeting_to_email(msg:EmailMessage) -> None:
    """Sends the greeting to the celebrant's email"""
    with smtp.SMTP(host="smtp.gmail.com", port=587, timeout=10) as conn:
        conn.starttls()
        conn.login(user=sender_email, password=sender_email_pw)
        conn.send_message(msg=msg)


# Main program
celebrant = check_birthday(file=birthdays)

if celebrant:
    msg = construct_greeting(templates=templates_paths, celebrant=celebrant)
    send_greeting_to_email(msg=msg)
    print(f"Sent a birthday greeting to {celebrant['name']}.")
else:
    print("There are no birthday celebrants today.")


