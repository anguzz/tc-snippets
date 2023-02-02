import smtplib
from email.mime.text import MIMEText


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()



subject = "Test Email Subject"
body = "This is the body of the text message"
sender = "santoyox714@gmail.com"
recipients = ["santoyox714@gmail.com"]
password = "" #enter your pw here 



send_email(subject, body, sender, recipients, password)