#python -m smtpd -c DebuggingServer -n localhost:1025
import smtplib, ssl
sender_email = "automationtest3798@gmail.com"
receiver_email = "dixit.2@iitj.ac.in"
message = """\
Subject: Hi there

This message is sent from Python."""


port = 465  # For SSL, SSL (Secure Sockets Layer) and TLS (Transport Layer Security)
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("automationtest3798@gmail.com", password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, message)