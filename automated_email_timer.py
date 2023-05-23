import smtplib
from email.message import EmailMessage 
import ssl
import time
import datetime

name = input('Enter your name: ')
address_sender = input('Enter the email address of the sender: ')
password_sender = input('Enter the email password: ')
input_address_recipients = input('Enter the address of all recipients: ')
address_recipients = list((input_address_recipients))
subject = input('Enter the subject of the mail: ')
body = input('Enter the body of the mail: ')
mail_time = datetime.datetime.now()

email_msg = EmailMessage()

email_msg['From'] = address_sender
email_msg['To'] = ','.join(input_address_recipients)
email_msg['Subject'] = subject
email_msg.set_content(body)

#create a default connection if its taking time to send bulk message
context = ssl.create_default_context()


def perform_task():


 with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as mysmtp:
    mysmtp.login(address_sender,password_sender)
    mysmtp.sendmail(address_sender,input_address_recipients, email_msg.as_string())
    print('Hi your message has been sent successfully at:', mail_time)
        

       #send mail every 10 minutes
while True:
    perform_task()
    time.sleep(600)  # 10 minutes = 10 * 60 seconds
