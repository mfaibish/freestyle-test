# free.py

import json
from dotenv import load_dotenv
import os

import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

request_url = "http://api.tvmaze.com/schedule/full"
response = requests.get(request_url)
parsed_response = json.loads(response.text)



DOCUMENT_ID = os.environ.get("DOCUMENT_ID", "OOPS")
SHEET_NAME = os.environ.get("SHEET_NAME", "Shows")

#
# AUTHORIZATION
#

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google_api_credentials.json")

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)

#
# READ SHEET VALUES
#

client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>

doc = client.open_by_key(DOCUMENT_ID) #> <class 'gspread.models.Spreadsheet'>


print("-----------------")
print("SPREADSHEET:", doc.title)
print("-----------------")

sheet = doc.worksheet(SHEET_NAME) #> <class 'gspread.models.Worksheet'>

shows = sheet.get_all_records() #> <class 'list'>


for show in shows:
    print(shows) #> <class 'dict'>






