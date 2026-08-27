import os
from dotenv import load_dotenv
import smtplib as smtp
from email.message import EmailMessage

# Initialize .env variables into local memory
load_dotenv()

# Get credentials stored in local memory
sender_email = os.getenv("WORK_GMAIL_UN")
sender_email_pw = os.getenv("WORK_GMAIL_APP_PW")
recipient_email = os.getenv("PERSONAL_GMAIL_UN")

# Optional: creating email message using the built in email.message module for cleaner headers
msg = EmailMessage()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = "Test Email"
msg.set_content("This is a test email sent using SMTP Py module.")

# Setup connection using SMTP module
# SMTP address for gmail = smtp.gmail.com, PORT 587 is std port for sending email via SMTP, timeout waits for 10s and throws an error if no conn was established
with smtp.SMTP ("smtp.gmail.com", port=587, timeout=10) as conn:

    # Establish a secure connection to the servers using TLS
    # This should always come first before logging in
    conn.starttls()

    # Login using credentials
    conn.login(user=sender_email, password=sender_email_pw)

    # Send sample email
    # When using EmailMessage objects, the .send_message should be used because it parses the obj, rather than the old .sendmail method which expects raw strings
    conn.send_message(msg=msg)

# Print out confirmation
print("Successfully sent an email!")