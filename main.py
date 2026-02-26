from fastapi import FastAPI
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import os
import json

app = FastAPI()

SHEET_NAME = "ConfiText Content Engine"

def load_credentials():
    creds_json = os.environ.get("GOOGLE_CREDS")
    creds_dict = json.loads(creds_json)
    return Credentials.from_service_account_info(
        creds_dict,
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
    )

@app.get("/run-analysis")
def run_analysis():
    creds = load_credentials()
    client = gspread.authorize(creds)

    sheet = client.open(SHEET_NAME).sheet1
    data = sheet.get_all_records()

    if not data:
        return {"message": "No data found"}

    df = pd.DataFrame(data)

    top_video = df.sort_values(by="Views", ascending=False).iloc[0]

    return {
        "Top Angle": top_video["Angle "],
        "Top Hook": top_video["Hook"],
        "Views": top_video["Views"],
        "Retention": top_video["3s_Retention"],
        "Avg Watch": top_video["Avg_Watch"],
        "Saves": top_video["Saves"]
    }
