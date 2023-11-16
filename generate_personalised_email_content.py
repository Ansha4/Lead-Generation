import openai
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Set up OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Set up Google Sheets API credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile("YOUR_GOOGLE_CREDENTIALS.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheets document
spreadsheet = client.open("Your Spreadsheet Name")
worksheet = spreadsheet.get_worksheet(0)  # Change the index to the appropriate sheet

# Read lead data into a pandas DataFrame
lead_data = worksheet.get_all_records()
df = pd.DataFrame(lead_data)

# Function to generate personalized email content
def generate_personalized_email(lead):
    # You can customize the email template with placeholders like {Name} and {BusinessDetails}
    template = f"Hello {lead['Name']},\n\nI hope you are doing well. We are excited to learn more about your business, {lead['BusinessDetails']}."
    
    # Use the OpenAI ChatGPT API to complete the email
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=template,
        max_tokens=100  # Adjust max_tokens as needed for the desired email length
    )
    
    email_content = response.choices[0].text.strip()
    return email_content

# Generate personalized emails for each lead and store them in a new column
df['EmailContent'] = df.apply(generate_personalized_email, axis=1)

# Print or save the DataFrame with personalized email content
print(df[['Name', 'EmailContent']])

# You can save the DataFrame to a new Google Sheet, CSV, or any other desired format
# df.to_csv('personalized_emails.csv', index=False)
