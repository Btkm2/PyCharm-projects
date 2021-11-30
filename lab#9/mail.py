import smtplib, ssl

def send_mail(email,name):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = email  # Enter your address
    receiver_email = "beketmuratbek57@gmail.com"  # Enter receiver address
    password = "zigMak-nocsac-dunma8"
    message = """\
    Subject: Hi there

    Hey {}.""".format(name)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)