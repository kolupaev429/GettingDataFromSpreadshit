from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = '1MEsqTX4rYJTSvKRAgTizUchZ7PNuPLFMutNrFArf6eM'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:D100',
    majorDimension='ROWS'
).execute()

number_of_strings = len(values['values'])

recipients = []
for i in range(number_of_strings):
    print(i + 1, values['values'][i])
n = int(input("Введите номер строки актуального записавшегося: "))
for i in range(n - 1, number_of_strings):
    recipients.append(values['values'][i][3])
