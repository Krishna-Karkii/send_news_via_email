import os
import smtplib
import ssl

HOST = "smtp.gmail.com"
PORT = 465
CONTEXT = ssl.create_default_context()
RECEIVER_MAIl = "emailexperimental70@gmail.com"
PASSWORD = "gsbs sney zgvo vhfr"


def send_mail(user_email,
              message):

    #     message = f"""\
    # Subject: News from {user_email}\n
    # From: {user_email}\n
    # {message}"""
    with smtplib.SMTP_SSL(HOST, PORT, context=CONTEXT) as server:
        server.login(RECEIVER_MAIl, PASSWORD)
        server.sendmail(user_email, RECEIVER_MAIl, message)

