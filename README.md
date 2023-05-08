# SheetMagic
SheetMagic: A Python script that magically appends data from a CSV file to a Google Sheets document.


#About This Project

This Python script reads data from a CSV file and appends it to a Google Sheet. However, the script is not optimized and there are several improvements that can be made.

Improvements are needed for the script by implementing the following features(Help me implement them):

  ==>  Parse the CSV file correctly: The script currently copies all values after the colons and pastes them into the Google Sheet. However, some values may contain special characters or units that should be removed before appending to the sheet.

==>  Match the CSV headers to the Google Sheet columns: The headers in the CSV file do not match the order of the columns in the Google Sheet. The script should be updated to locate the correct columns in the sheet and append the values in the appropriate cells.

==>  Ignore unnecessary data: Not all values in the CSV file should be appended to the Google Sheet. The script should be updated to only append the necessary values.

==>  Error handling: The script should be able to handle errors such as incorrect file paths or missing columns in the Google Sheet.


#Installation

This project can be run by installing a few pip dependencies by running the following commands.

pip install gspread oauth2client

Then git clone this repo.

Then run the script with

python trade-gspread.py

You should see data being appended in the following google sheet.
https://docs.google.com/spreadsheets/d/1D3u8lRRF5-hz7LVKO8X92PlKkkpbhX7ZLvCGFYiHRIs/edit?usp=sharing
