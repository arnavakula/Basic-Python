import smtplib
from email.mime.text import MIMEText

body = 'Testing email from python client'
msg = MIMEText(body)
msg['From'] = "akula.arnav@gmail.com"
msg['To'] = "akula.arnav@gmail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com', 587) #creating server

server.starttls() #enable connection

server.login("akula.arnav@gmail.com", "vreck479don")

server.send_message(msg)

print("Mail sent")

server.quit()

