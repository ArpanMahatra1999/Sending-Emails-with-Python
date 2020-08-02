# importing libraries
import smtplib
import imghdr
from email.message import EmailMessage

# define variables
EMAIL_ADDRESS = 'Your Email here'
EMAIL_PASSWORD = 'Your Password here'

# contacts of receivers
contacts = ['spranish45@gmail.com', 'anjelikasah98@gmail.com']

# message details
msg = EmailMessage()
msg['Subject'] = 'Just to Test Email'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)
msg.set_content('Here are the attachments...')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1>Hello There</h1>
    </body>
</html>""", subtype='html')

# for sending message
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
