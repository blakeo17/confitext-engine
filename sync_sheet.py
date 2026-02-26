import gspread
from google.oauth2.service_account import Credentials
import json
import os
import pandas as pd

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Load credentials from Railway environment variable
creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS_JSON"])

creds = Credentials.from_service_account_info(
    creds_dict,
    scopes=SCOPES
)

client = gspread.authorize(creds)

# Open your Google Sheet
sheet = client.open("ConfiText Content Engine").sheet1


def sync_metrics():
    print("Syncing metrics from Google Sheet...")

    # Get all records
    records = sheet.get_all_records()

    if not records:
        print("No data found in sheet.")
        return

    df = pd.DataFrame(records)

    # Save locally
    os.makedirs("data", exist_ok=True)
    df.to_json("data/metrics.json", orient="records", indent=2)

    print("Metrics synced successfully.")


if __name__ == "__main__":
    sync_metrics()
