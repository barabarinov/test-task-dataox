import gspread
import json
from dotenv import load_dotenv
import os

load_dotenv()

gc = gspread.service_account_from_dict(json.loads(os.getenv('CREDENTIALS')))

sh = gc.open("Apartments")
wks = sh.worksheet('List1')


def save_info_to_google_sheets(list_of_apartment_data):
    wks.insert_rows(values=list_of_apartment_data, row=2)
    print(f'✅ Google SpreadSheet has been filled!')
