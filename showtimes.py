# showtimes.py

import json
from dotenv import load_dotenv
import os
import datetime
import operator

import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

def date_format(x):
    today_date = x.strftime("%A, %B %d, %Y")
    return today_date


# LOAD API DATA FROM TVMAZE
request_url = "http://api.tvmaze.com/schedule/full"
response = requests.get(request_url)
parsed_response = json.loads(response.text)


# gspread package github notes: https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/gspread.md
# READ IN SECRET KEYS
DOCUMENT_ID = os.environ.get("DOCUMENT_ID", "OOPS")
SHEET_NAME = os.environ.get("SHEET_NAME", "Shows")
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")
SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")

#
# AUTHORIZATION OF GOOGLE SHEET
#

CREDENTIALS_FILEPATH = os.path.join(os.path.dirname(__file__), "auth", "google_api_credentials.json")

AUTH_SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets", #> Allows read/write access to the user's sheets and their properties.
    "https://www.googleapis.com/auth/drive.file" #> Per-file access to files created or opened by the app.
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILEPATH, AUTH_SCOPE)

#
# READ GOOGLE SHEET VALUES
#

client = gspread.authorize(credentials) #> <class 'gspread.client.Client'>

doc = client.open_by_key(DOCUMENT_ID) #> <class 'gspread.models.Spreadsheet'>

print("-----------------")
print("SPREADSHEET:", doc.title)
print("-----------------")

sheet = doc.worksheet(SHEET_NAME) #> <class 'gspread.models.Worksheet'>
shows = sheet.get_all_records() #> <class 'list'> - list of shows from google sheet 

# OUTPUTS 


matching_shows = []
for row in shows: 
    show_names = [p for p in parsed_response if p["_embedded"]["show"]["name"] == row["Name"]] # puts shows from api in a smaller list based on google spreadsheet values  
    
    try:
        name = show_names[0]["_embedded"]["show"]["name"]
        airdate = show_names[0]["airdate"]
        airtime = show_names[0]["airtime"]
        shows_dict = {"name": name, "date": airdate, "time": airtime}
        matching_shows.append(shows_dict)
        #print(show_names[0]["_embedded"]["show"]["name"] + " " + show_names[0]["airdate"])
        #print(name + " " + airdate)
    except:
       name = row["Name"]
       print(f"{name} is not on this week")
       next

print("-----------------------------")
matching_shows = sorted(matching_shows, key=operator.itemgetter('date'))
for match in matching_shows:
    print("..." + match["date"] + " - " + match["time"] + ": " + match["name"])




# SEND EMAIL
# sendgrid package notes - https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/sendgrid.md#email-templates

date = datetime.datetime.now()
today_date = date_format(date)

print("-----------------------------")
print("SENDING RESULTS IN AN EMAIL ....")
print("-----------------------------")
template_data = {
    "date": today_date,
    "shows": matching_shows          
}

client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client))

message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS)
print("MESSAGE:", type(message))

message.template_id = SENDGRID_TEMPLATE_ID

message.dynamic_template_data = template_data

try:
    response = client.send(message)
    print("RESPONSE:", type(response))
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as e:
    print("OOPS", e)


#matching_shows = []
#for i in [1, 2, 3, 4, 5]:
#    d = {"number": i, "name": "thing"}
#    matching_shows.append(d)
