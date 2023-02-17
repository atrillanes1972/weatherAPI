import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "curzekonrad72@gmail.com"
password = "cpoiufulxpkfztnx"

receiver = "hlupercal40k@gmail.com"
context = ssl.create_default_context()

message = """
Subject: Testing Email!
Hi, how are you!
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username,password)
    server.sendmail(username, receiver,message)