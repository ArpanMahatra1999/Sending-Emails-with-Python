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

files = ['starrynight.jpg']

# looping through files
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        file_type = imghdr.what(f.name)  # for images

    # for attaching images in message
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

# for sending message
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
