from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account #this is for the scopes/sheet access
import pandas as pd
import numpy as np
import funcs as func

# sheets access through service account
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'key.json'
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of a sample spreadsheet. 
#spread sheet id is the the letters in the url between d/ and /edit
SAMPLE_SPREADSHEET_ID = '1K3HniW6VJZx4LDcyRpfzIDmW9HBv7HzghA7jQOMi-Hg' #to get this we will have to have some sorta of menu interface.

try:
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    SAMPLE_RANGE_NAME = 'Sheet1!A1:B13' #we will need to have user input for this
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[1]))



except HttpError as err:
    print(err)

