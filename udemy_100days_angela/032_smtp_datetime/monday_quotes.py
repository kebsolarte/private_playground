import os
from dotenv import load_dotenv
import smtplib as smtp
from email.message import EmailMessage
import datetime as dt
import random

# Initialize .env variables
load_dotenv()


# Get credentials
sender_email = os.getenv("WORK_GMAIL_UN")
sender_email_pw = os.getenv("WORK_GMAIL_APP_PW")
recipient_email = os.getenv("PERSONAL_GMAIL_UN")


# Load quotes file into a list
file_path = "quotes.txt"

with open(file_path, mode='r') as file:
    quotes = [row.strip() for row in file.readlines()]


# Create EmailMessage object
email_msg = EmailMessage()
email_msg['From'] = sender_email
email_msg['To'] = recipient_email
email_msg['Subject'] = "Monday motivational quote!"
email_msg.set_content(random.choice(quotes))


# Send_quote_to_email function
def send_quote_to_email(msg: EmailMessage):
    with smtp.SMTP(host="smtp.gmail.com", port=587, timeout=10) as conn:
        conn.starttls()
        conn.login(user=sender_email, password=sender_email_pw)
        conn.send_message(msg=msg)


# Main program
# Check if today is Monday
if dt.datetime.now().weekday() == 0:
    # Send a random quote to email
    send_quote_to_email(msg=email_msg)
    print("Motivational quote sent!")
