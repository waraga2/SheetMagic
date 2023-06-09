import gspread
import re
from oauth2client.service_account import ServiceAccountCredentials
import csv

HEADER_MAPPING = {
    "Market type": "Market",
    "Profit": "Realized Profit",
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

def extract_data(csv_file, sheet_name, worksheet_name):
    with open(csv_file, 'r') as file:
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
    row_str = ''.join(row)
    key, value = row_str.split(":", 1)
    key = key.strip()
    value = value.strip()
    return key, value

def transform_value(key, value):
    value = value.replace("'", "")

    if key == "Max Drawdown":
        value = value.split("(")[0].strip()
        value = value.replace("$", "").replace("-", "")
        try:
            return float(value)
        except ValueError:
            return value
    elif key == "Stake" or key == "Profit" or key == "Ratio Avg Win/Loss" or key == "Comment" or key == "Market type":
        try:
            return float(value)
        except ValueError:
            return value
    elif key == "Time Playing":
        if value.startswith("'"):
            value = value[1:]
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

def convert_time_to_minutes(time_str):
    time_parts = re.findall(r'\d+', time_str)
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2])

    total_minutes = hours * 60 + minutes + (1 if seconds >= 30 else 0)
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    return total_minutes, formatted_time

def append_to_sheets(csv_file, sheet_name, worksheet_name):
    extracted_data = extract_data(csv_file, sheet_name, worksheet_name)
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_name, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).worksheet(worksheet_name)

    row_values = [''] * sheet.col_count

    for key, value in extracted_data.items():
        column = sheet.find(HEADER_MAPPING[key]).col
        row_values[column - 1] = value

    sheet.append_row(row_values)

    # Get the last row number
    last_row = len(sheet.get_all_values())

# Get the cell address for the last row in column N
    row_address = f"{last_row}"

    # Get the cell address for the last row in column N
    cell_address = f"N{last_row}"

    try:
        # Get the cell value
        cell_value = sheet.acell(cell_address).value

        # Convert the time value to minutes and format it as HH:MM:SS
        total_minutes, formatted_time = convert_time_to_minutes(cell_value)

        # Update the cell with the converted value
        sheet.update_acell(cell_address, formatted_time)

        # Output success message
        #print('Cell', cell_address, 'updated successfully.')
        #print('Converted time:', formatted_time)
        print("Data appended successfully.")
        print("Worksheet name: ", worksheet_name)
        print("Sheet file name:", sheet_name)
        print("Appended row number:", row_address)

    except gspread.exceptions.APIError as e:
        print('Error updating cell:', str(e))

def cell_cleaner(sheet_name, worksheet_name):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_name, scope)
    client = gspread.authorize(credentials)

    sheet = client.open(sheet_name).worksheet(worksheet_name)

    last_row = len(sheet.get_all_values())

    column_names = ['Target Profit', 'Stop Loss', 'Net Gross Risk', 'Trade / Time', 'Realized Profit']

    for column_name in column_names:
        column = sheet.find(column_name)
        sheet.update_cell(last_row, column.col, "")

if __name__ == '__main__':
    csv_file = "tradedata.csv"
    sheet_name = "Trading Sheet"
    worksheet_name = "Rise Fall | Fast Profit"

    json_keyfile_name = "my-trading-project-384611-98e812573160.json"
    append_to_sheets(csv_file, sheet_name, worksheet_name)
    cell_cleaner(sheet_name, worksheet_name)
