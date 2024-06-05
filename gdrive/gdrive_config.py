import gspread
from google.oauth2.service_account import Credentials
# from gspread import Client

# Установка параметров подключения
scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
    ]

# Путь к файлу ключа доступа JSON
credentials = Credentials.from_service_account_file('.keys/.credentials.json', scopes=scope)
# gs: Client =
# Таблица fishstorage
fishstorage_table_id = '1EiYYUHQqJZK0MY0-2XIk6rDV52md46yScl_i6hanXIY'

def get_google_spreadsheet(spreadsheet_id):
    # Аутентификация и установка подключения
    client = gspread.authorize(credentials)
    # Открытие листа таблицы для чтения
    sh = client.open_by_key(spreadsheet_id)
    return sh