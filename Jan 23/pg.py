'''
Write a Python script that prompts the user for their email address, recipient emailaddress, subject, and message body.
Then, use the smtpliblibrary to send the emailusing the user's email address and password.
Use proper exception handling. Usemailtrap service to debug your code.
'''

# importing the libraries
import smtplib
from email.mime.text import MIMEText
from socket import gaierror

# try block
try:

    # sender name/ email address
    email_from = 'jerinraju868@gmail.com'

    # reciver name/email address
    email_to = 'jerinraju868@gmail.com'

    # email subject
    email_subject = 'Sample mail'

    # email body
    email_body = 'This is a sample mail from python backend developer'

    # using MIMEtex() function the message is setting by passing the email body
    message = MIMEText(email_body)

    # from address
    message['From'] = email_from

    # to address
    message['To'] = email_to

    # subject
    message['Subject'] = email_subject

    # smtp server
    smtp_server = 'smtp.mailtrap.io'

    # smtp port
    smpt_port = 465

    # username of the sender email
    smtp_username = 'c9afbb9b64a4fe'

    # mail password of the sender
    smtp_password = '99d9eb81e7a8ee'

    # connecting the smtp library to smtp function by passing the smtp server and port number 
    server = smtplib.SMTP(smtp_server, smpt_port)

    # starts the tls 
    server.starttls()

    # login function by passing the sender username and password
    server.login(smtp_username, smtp_password)

    # sending the email by usig the sendmail() by passing the email address of the sender and reciver and the message as string
    server.sendmail(email_from, email_to, message.as_string())

    # quiting the server
    server.quit()

    # displaying the successful message after sending the mail
    print('Mail send successfully..')

# except block for catching the connection error
except (gaierror, ConnectionRefusedError):

    # printing the error message
    print('\n Failed to connect to the server. Check your internet connection.\n')

# except block for catching the credentials errors
except smtplib.SMTPServerDisconnected as s:

    # displaying the error message
    print('\nInvalid credentials...!\n',s)

# except block for  handling the all other errors
except Exception as e:

    # displaying the error message
    print('\nSomething went wrong...!\n',e)