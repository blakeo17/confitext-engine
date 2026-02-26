import gspread
from google.oauth2.service_account import Credentials
import json

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_file(
    "data/google_credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

# Open your sheet by name
sheet = client.open("ConfiText Content Engine").sheet1

data = sheet.get_all_records()

with open("data/metrics.json", "w") as f:
    json.dump(data, f, indent=2)

print("Metrics synced successfully.")

