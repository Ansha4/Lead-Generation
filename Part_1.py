import csv
import requests
from bs4 import BeautifulSoup

# Define the URL to scrape (replace with your desired location and industry)
url = "https://www.geeksforgeeks.org/data-structures/"
# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Create a list to store scraped data
data_list = []

# Find and extract business information
for item in soup.find_all("div", class_="section-result-details"):
    name = item.find("h3", class_="section-result-title").text.strip()
    address = item.find("span", class_="section-result-location").text.strip()
    phone = item.find("span", class_="section-result-phone-number").text.strip()
    email = ""  # You may need to implement email scraping separately

    data_list.append([name, address, phone, email])

# Store the scraped data in a CSV file
with open("scraped_data.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Name", "Address", "Phone", "Email"])
    csvwriter.writerows(data_list)
