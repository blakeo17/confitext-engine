import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# Google Sheets scopes
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Load credentials from local JSON file
creds = Credentials.from_service_account_file(
    "google_credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

# Replace with your actual sheet name
SHEET_NAME = "ConfiText Metrics"

def sync_sheet():
    print("Syncing sheet...")

    sheet = client.open(SHEET_NAME).sheet1
    records = sheet.get_all_records()

    if not records:
        print("No data found in sheet.")
        return []

    df = pd.DataFrame(records)

    # Save to local JSON file for analysis
    df.to_json("data/metrics.json", orient="records")

    print("Metrics synced successfully.")
    return records
