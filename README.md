# freestyle-project

An app that allows a user to input television shows into a google spreadsheet and return what day and time the next episode of the show is

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

Fork this repository under your own control, then clone or download the resulting repository onto your computer. Then navigate there from the command line:

```sh
cd freestyle-test
```

> NOTE: subsequent usage and testing commands assume you are running them from the repository's root directory.

Use Anaconda to create and activate a new virtual environment, called "showtimes-env":

```sh
conda create -n showtimes-env python=3.7 # (first time only)
conda activate showtimes-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
pip install pytest
```

## SETUP
### Google Spreadsheet
#### API Credentials 
Visit the Google Developer Console (https://console.developers.google.com/cloud-resource-manager). Create a new project, or select an existing one. Click on your project, then from the project page, search for the "Google Sheets API" and enable it. Also search for the "Google Drive API" and enable it.

From either API page, or from the API Credentials page (https://console.developers.google.com/apis/credentials), follow a process to create and download credentials to use the APIs. Fill in the form to find out what kind of credentials:

    API: "Google Sheets API"
    Calling From: "Web Server"
    Accessing: "Application Data"
    Using Engines: "No"

The suggested credentials will be for a service account. Follow the prompt to create a new service account with a role of: "Project" > "Editor", and create credentials for that service account. Download the resulting .json file. Create an "auth" directory within the repo and store the file in there with the name "google_api_credentials.json" (i.e. "freestyle-project/auth/google_api_credentials.json").

#### Configuring Spreadsheet Document
Create a google spreadsheet of your own or use this one as an example. (https://docs.google.com/spreadsheets/d/1smv-9HsQCDYY7lKLrKqj75LXhrKPwvtpIYOp_67ioYE/edit#gid=0) Note the document's unique identifier (e.g. 1smv-9HsQCDYY7lKLrKqj75LXhrKPwvtpIYOp_67ioYE) from its URL, and store the identifier in an environment variable called DOCUMENT_ID in a .env file

If you create your own, make sure it contains a sheet called "This week's lineup" with a column header "Name". And modify the document's sharing settings to grant "edit" privileges to the "client email" address located in the credentials file. Create another environment variable called SHEET_NAME in the same .env file created earlier.


### SendGrid
If you don't already have one, sign up for a SendGrid account (https://signup.sendgrid.com/), then click the link in a confirmation email to verify your account. Then create an API Key with "full access" permissions.

Store the API Key value in an environment variable called SENDGRID_API_KEY. Also set an environment variable called MY_EMAIL_ADDRESS to be the email address you just associated with your SendGrid account (e.g. "abc123@gmail.com") in the same .env file created earlier.

#### SendGrid Email Template
Navigate to https://sendgrid.com/dynamic_templates and press the "Create Template" button on the top right. Give it a name like "Show-time", and click "Save". At this time, you should see your template's unique identifier (e.g. "d-b902ae61c68f40dbbd1103187a9736f0"). Copy this value and store it in an environment variable called SENDGRID_TEMPLATE_ID in the .env file created earlier. 

In the SendGrid platform, click "Add Version" to create a new version of this template and select the "Code Editor" as your desired editing mechanism.

At this point you should be able to paste the following HTML into the "Code" tab, and the corresponding example data in the "Test Data" tab:

"Code" tab:
```sh
<img src= "https://s.pngkit.com/png/small/243-2434352_tv-network-logos-png-png-tv-network-logos.png">

<h3>Here's what TV shows are on this week!</h3>

<p>Today's Date: {{this.date}}</p>

<ul>
{{#each shows}}
  <li>{{this.date}} - {{this.time}} ... {{this.name}}</li>
{{/each}}
</ul>
```
"Test Data" tab:
```sh
{
  
    "date": "July 4th, 2019",
    "shows":[
        {"id":1, "name": "show 1", "date": "2019-06-27", "time": "15:00"},
        {"id":2, "name": "show 2", "date": "2019-07-01", "time": "22:00"},
        {"id":3, "name": "show 3", "date": "2019-06-30", "time": "16:00"}
    ]
}
```

Finally, configure the template's subject by clicking on "Settings" in the left sidebar. Choose an email subject like "This weeks lineup is...". Then click "Save Template".



## USAGE 

```py
python showtimes.py
```


## TESTING
Run tests:

```sh
pytest
```


## ATTESTATIONS
1. Prerequisites and Installation sections adapted from https://github.com/prof-rossetti/robo-advisor-demo-2019
2. SendGrid sections adapted from https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/sendgrid.md
3. Google Spreadsheet sections adapted from https://github.com/prof-rossetti/nyu-info-2335-201905/blob/master/notes/python/packages/gspread.md