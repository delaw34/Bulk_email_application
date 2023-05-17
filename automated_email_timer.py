import smtplib
from email.message import EmailMessage 
import ssl
import time
name = "sender_name"
address_sender = 'your_sender_email'
password_sender =  'your_sender_password'
input_address_recipients = 'recipient_email'
address_recipients = input_address_recipients.split(',')
subject = 'Automatic Email'
body =  'This is an automatic email sent every 10 minutes.'

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
    print('Hi your message has been sent successfully')
        

       #send mail every 10 minutes
while True:
    perform_task()
    time.sleep(600)  # 10 minutes = 10 * 60 seconds
