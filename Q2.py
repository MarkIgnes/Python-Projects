import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "sowhynot24@gmail.com"  # My Gmail email
password = ""  # Where the Gmail account password goes
send_to_email = "sowhynot23@gmail.com"  # the recipient of the Email
subject = 'This is the Subject'  # The subject line
body = 'This is the body. Professor Lin is the best.'  # The body of the email

msg = MIMEMultipart()
msg['From'] = "God@Microsoft.com"
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the Gmail server
server.starttls()  # Using TLS
server.login(email, password)  # Login to the email server
text = msg.as_string()
server.sendmail(email, send_to_email, text)  # Send the email
server.quit()  # Logout of the email server
