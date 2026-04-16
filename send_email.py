import smtplib, ssl

SENDER_EMAIL = "*YOUR_EMAIL*" # email used to send message
SENDER_EMAIL_PWD = "YOUR_EMAIL_PASSWORD" # password for your email
RECEIVER_EMAIL = "*RECEIVERS_EMAIL*" # sends email to that address



def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = SENDER_EMAIL
    password = SENDER_EMAIL_PWD

    receiver = RECEIVER_EMAIL
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)