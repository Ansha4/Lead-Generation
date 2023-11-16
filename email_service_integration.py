import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "your@gmail.com"
sender_password = "your_password"
recipient_email = "recipient@example.com"
subject = "Hello, World!"
message = "This is a test email sent from Python."

# Create the MIME object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Connect to the Gmail SMTP server
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    
    # Send the email
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
