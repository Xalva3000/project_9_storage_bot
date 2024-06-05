import gspread
import pandas as pd
from gdrive.gdrive_config import credentials, fishstorage_table_id


def get_fishstorage_total():

    # Аутентификация и установка подключения
    client = gspread.authorize(credentials)

    # Открытие листа таблицы для чтения
    sheet = client.open_by_key(fishstorage_table_id).worksheet('total')

    # Получение данных в формате DataFrame
    df = pd.DataFrame(sheet.get_all_records())
    total = df[['name', 'weight', 'freepos', 'freeweight']]

    return total[total['name'] != '---']
