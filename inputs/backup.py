import httplib2
import googleapiclient.discovery
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import pathlib
import pandas as pd
from .models import back

def backup(name,deleter):
    CREDENTIALS_FILE = str(pathlib.Path(__file__).parent.resolve())+'/backup-334515-e0b541a9ad5d.json'  # Имя файла с закрытым ключом, вы должны подставить свое
    # Читаем ключи из файла
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе

    driveService = googleapiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API

    file_metadata = {'name': f'{name}.xlsx'}
    media = MediaFileUpload(str(pathlib.Path(__file__).parent.resolve())+'/backup/'+name+'.xlsx',
                            mimetype='application/vnd.ms-excel')
    file = driveService.files().create(body=file_metadata,
                                       media_body=media,
                                       fields='id').execute()


    print('File ID: %s' % file.get('id'))
    item = back(file = str(file.get('id')))
    item.save()

    access = driveService.permissions().create(
        fileId = file.get('id'),
        body = {'type': 'user', 'role': 'writer', 'emailAddress': 'opsreservecopy@gmail.com'},  # Открываем доступ на редактирование
        fields = 'id'
    )
    access.SendNotificationEmail = False
    access.execute()


    # print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)