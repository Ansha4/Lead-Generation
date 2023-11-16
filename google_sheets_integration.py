import gspread
import csv
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials JSON file (replace with your JSON file)
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("client_secret_145061442087-1tsa2f84h415iai82h4v7rf2nm548vpm.apps.googleusercontent.com.json", scope)

# Authenticate with Google Sheets API
client = gspread.authorize(credentials)

# Open the Google Sheets document
spreadsheet = client.open("Part 1")

# Select a specific worksheet (or create one if it doesn't exist)
worksheet = spreadsheet.get_worksheet(0)

# Load the scraped data from the CSV file
with open("scraped_data.csv", "r") as csvfile:
    data = list(csv.reader(csvfile))

# Append the data to the Google Sheets document
worksheet.append_rows(data)
