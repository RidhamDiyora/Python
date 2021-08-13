import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("email-id","password")
server.sendmail("email-id","email-id","Your message")
server.quit()
