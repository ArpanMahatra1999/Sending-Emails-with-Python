import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("Type your email here", "Type your password here")
server.sendmail("Type your email here", "Type receiver email here", f'Subject:Hello\n\nBrother')

server.quit()
