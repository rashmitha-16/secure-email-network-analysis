Apart from using disposable email, you can also send encrypted messages securely using any account and Python.

🧪 Sample Script: test.py


import smtplib

email = input("SENDER email:      ")
receiver = input("RECEIVER email:    ")

subject = input("Subject:   ")
message = input("Message:   ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
# Follow with login and sending logic...


💡 This basic script takes sender and receiver email, a subject, and message body, then prepares it for sending via Gmail SMTP (smtp.gmail.com).

You can modify this script to send the encrypted .asc content instead of plain text.


✅ Next Steps
Add server.login(sender_email, password) after server.starttls()
Use server.sendmail(email, receiver, text) to send the message

Don’t forget to enable "App Passwords" or "Less secure app access" in your Gmail settings if using basic authentication







