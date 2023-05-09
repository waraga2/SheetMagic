import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

# Define the name of the CSV file and Google Sheets file
CSV_FILE = "tradedata.csv"
SHEETS_FILE = "trading sheet"

# Define the mapping of CSV headers to sheets headers
HEADER_MAPPING = {
    "Market type": "Market",
    "Stake": "Stake",
    "Trades": "Trades",
    "Max Consecutive Losses": "Consec. Loss",
    "Highest Stake": "Highest Stake",
    "Max Drawdown": "Max Drawdown",
    "Max Consecutive Wins": "Consec. Wins",
    "Ratio Avg Win/Loss": "Win:Loss Ratio",
    "Wins": "Winrate %",
    "Time Playing": "Overall Time",
    "Avg Profit Per Trade": "Profit / Trade",
    "Comment": "Comment"
}

def extract_data():
    with open(CSV_FILE, 'r') as file:
        data = csv.reader(file)
        extracted_data = {}
        for row in data:
            try:
                key, value = extract_key_value(row[0])
                extracted_data[key] = transform_value(key, value)
            except KeyError:
                pass
    return extracted_data

def extract_key_value(row):
    split_row = row.split(":", 1)
    key = split_row[0].strip()
    value = split_row[1].strip() if len(split_row) > 1 else ""
    return key, value

def transform_value(key, value):
    if key == "Winrate %":
        return value.split("(")[1].replace("%)", "")
    elif key == "Profit / Trade":
        return value.replace("$", "")
    elif key == "Max Drawdown":
        return value.split("(")[0].strip()
    else:
        return value

def append_to_sheets():
    extracted_data = extract_data()
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('my-trading-project-384611-98e812573160.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open(SHEETS_FILE).sheet1
    sheet.append_row(list(extracted_data.values()))

if __name__ == '__main__':
    append_to_sheets()
