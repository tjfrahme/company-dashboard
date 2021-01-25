import gspread
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# tells what api what it can access
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('my_cred.json', scope)

gc = gspread.authorize(creds) 

wks = gc.open('gspread_example_sheet').sheet1
data = wks.get_all_records()  #gets all values as a list of dictionaries
df = pd.DataFrame(data)


additional_info = {'Brand': 'Mercedes', 'Model': 'G-wagon'}
df = df.append(additional_info, ignore_index = True)

update_ws = gc.open('gspread_example_sheet').sheet1
gd.set_with_dataframe(update_ws, df)