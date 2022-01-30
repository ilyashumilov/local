import httplib2
import googleapiclient.discovery
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import pathlib
import pandas as pd

def ff():
    CREDENTIALS_FILE = str(pathlib.Path(__file__).parent.resolve())+'/backup-334515-e0b541a9ad5d.json'  # Имя файла с закрытым ключом, вы должны подставить свое
    # Читаем ключи из файла
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе

    driveService = googleapiclient.discovery.build('sheets', 'v4', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API

    sheet = driveService.spreadsheets()
    result = sheet.values().get(spreadsheetId='12OuUhqV_YEitz_2H0kCq9NQIn_gBfvUZuvD_zT32Dqo',
                                range='A3:N1000').execute()
    values = result.get('values', [])
    return values
