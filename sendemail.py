import smtplib
from_addr = 'saabay101@gmail.com'
to_addr = 'sajaymarsh@gmail.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}
{}
"""
message_to_send = message.format("Sajay", from_addr, "Me ofcourse", to_addr, "test mail", "This is a test message.")
#Credentials (if needed)
username = ''
password = ''
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()