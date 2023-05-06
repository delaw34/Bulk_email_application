#create an application that sends bulk email
import smtplib
from email.message import EmailMessage 
import ssl

name = input('Enter your name: ')
address_sender = input('Enter the email address of the sender: ')
password_sender = 'roqdsjxcrbhmvnxb'
input_address_recipients = input('Enter the address of all recipients: ')
address_recipients = input_address_recipients.split(',')
subject = input('Enter the subject of the mail: ')
body = input('Enter the body of the mail: ')


email_msg = EmailMessage()

email_msg['From'] = address_sender
email_msg['To'] = ','.join(input_address_recipients)
email_msg['Subject'] = subject
email_msg.set_content(body)

#create a default connection if its taking time to send bulk message
context = ssl.create_default_context()


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as mysmtp:
    mysmtp.login(address_sender,password_sender)
    mysmtp.sendmail(address_sender,input_address_recipients, email_msg.as_string())
    print('Hi Uzo message sent successfully to all cohorts')
#taking time in sending the bulk mails 