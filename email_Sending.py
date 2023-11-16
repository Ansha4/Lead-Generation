import gspread
from oauth2client.service_account import ServiceAccountCredentials
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# Google Sheets API authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('your-credentials.json', scope)
gc = gspread.authorize(credentials)

# Open the Google Sheet by its title
spreadsheet = gc.open('Your Google Sheet Title')
worksheet = spreadsheet.get_worksheet(0)  # Change 0 to the index of your sheet

# Get all records in the worksheet
records = worksheet.get_all_records()

# Gmail SMTP server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your-email@gmail.com'  # Your Gmail email address
smtp_password = 'your-app-password'  # App Password generated for Gmail

# Create a function to send personalized emails
def send_email(subject, to_email, message):
    try:
        # Create an SMTP connection
        smtp_conn = smtplib.SMTP(smtp_server, smtp_port)
        smtp_conn.starttls()  # Use TLS encryption
        smtp_conn.login(smtp_username, smtp_password)  # Log in to your Gmail account

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        smtp_conn.sendmail(smtp_username, to_email, msg.as_string())
        smtp_conn.quit()

        return True, "Email sent successfully"
    except Exception as e:
        return False, f"Email sending failed: {str(e)}"

# Iterate through the records and send emails
for record in records:
    # Customize the email content for each lead based on your data
    lead_name = record['Name']
    lead_email = record['Email']
    email_subject = f"Hello {lead_name}, Your Subject Here"
    email_body = f"Dear {lead_name},\n\nThis is a personalized message for you."

    success, status = send_email(email_subject, lead_email, email_body)

    # Log the status
    log_entry = f"{datetime.datetime.now()} - To: {lead_email}, Status: {'Success' if success else 'Failure'}, Message: {status}"
    with open('email_log.txt', 'a') as log_file:
        log_file.write(log_entry + '\n')
