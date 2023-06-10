import gspread
import re
from oauth2client.service_account import ServiceAccountCredentials
import csv

# Define the name of the CSV file and Google Sheets file
CSV_FILE = "tradedata.csv"
SHEETS_FILE = "trading sheet"

# Define the mapping of CSV headers to sheets columns
HEADER_MAPPING = {
    "Market type": "Market",
    "Trades": "Trades",
    "Stake": "Stake",
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
                key, value = extract_key_value(row)
                if key in HEADER_MAPPING:
                    extracted_data[key] = transform_value(key, value)
            except ValueError:
                pass
    return extracted_data

def extract_key_value(row):
    row_str = ''.join(row)  # Convert the list to a string
    key, value = row_str.split(":", 1)
    key = key.strip()
    value = value.strip()
    return key, value

def transform_value(key, value):
    value = value.replace("'", "")  # Remove apostrophes from cell values

    if key == "Max Drawdown":
        value = value.split("(")[0].strip()
        value = value.replace("$", "").replace("-", "")
        try:
            return float(value)
        except ValueError:
            return value
    elif key == "Stake" or key == "Ratio Avg Win/Loss" or key == "Comment" or key == "Market type":
        try:
            return float(value)
        except ValueError:
            return value
    elif key == "Time Playing":
        if value.startswith("'"):
            value = value[1:]  # Remove the leading apostrophe
        return value
    elif key == "Max Consecutive Losses" or key == "Max Consecutive Wins" or key == "Trades":
        return int(value)
    elif key == "Highest Stake" or key == "Avg Profit Per Trade":
        return float(value.replace("$", ""))
    elif key == "Wins":
        if '%' in value:
            x, y = value.split(' (%')
            rounded_value = round(float(y[:-1]))
            return rounded_value
    else:
        return value

def append_to_sheets():
    extracted_data = extract_data()
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('/home/jesse/Documents/Demo Trades/my-trading-project-384611-98e812573160.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open(SHEETS_FILE).sheet1

    # Create an empty list to hold the values in the desired column order
    row_values = [''] * sheet.col_count

    # Populate the row values with the extracted data based on the header mapping
    for key, value in extracted_data.items():
        column = sheet.find(HEADER_MAPPING[key]).col
        row_values[column - 1] = value

    # Append the row values to the Google Sheet
    sheet.append_row(row_values)

    # Get the last row number in column N
    last_row = len(sheet.col_values(14))

    # Get the cell address for the last row in column N
    cell_address = f"N{last_row}"

    try:
        # Get the cell value
        cell_value = sheet.acell(cell_address).value

        # Extract hours, minutes, and seconds using regular expressions
        time_parts = re.findall(r'\d+', cell_value)
        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        seconds = int(time_parts[2])

        # Convert time to minutes
        total_minutes = hours * 60 + minutes + (1 if seconds >= 30 else 0)

        # Update the cell with the converted value
        sheet.update_acell(cell_address, str(total_minutes))

        # Output success message
        print('Cell', cell_address, 'updated successfully.')

    except gspread.exceptions.APIError as e:
        print('Error updating cell:', str(e))

# Call append_to_sheets function
append_to_sheets()

print("Data appended to Google Sheet successfully.")

# Perform deletion operation
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/jesse/Documents/Demo Trades/my-trading-project-384611-98e812573160.json', scope)
client = gspread.authorize(credentials)
sheet_name = 'trading sheet'
worksheet_name = 'Rise Fall | Auto'
column_names = ['Target Profit', 'Stop Loss', 'Net Gross Risk', 'Trade / Time', 'Realized Profit']
sheet = client.open(sheet_name).worksheet(worksheet_name)
last_row = len(sheet.get_all_values())
for column_name in column_names:
    column = sheet.find(column_name)
    sheet.update_cell(last_row, column.col, "")