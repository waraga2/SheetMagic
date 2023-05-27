# SheetMagic
SheetMagic: A Python script that magically appends data from a CSV file to a Google Sheets document.


#About This Project

This Python script reads data from a CSV file and appends it to a Google Sheet.


#Installation

This project can be run by installing a few pip dependencies by running the following commands.

pip install gspread oauth2client

Then git clone this repo.

Download your own json key file from google cloud console follow these steps start reading the part where it says "Create a Json Key File" to save yourself some time==> 

https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/

or you could use my json key file for demonstration purposes only. Otherwise you should just make a copy of the spreadsheet provided and edit the two sections, each with two segments, they are "sheet file" and "work file". Just make sure you rename those sections accordingly. Also specify the path for your json key file in the code. There are two sections within the time-integers or time-numericals codes. Each section has two segments to fill up. The "sheet file name" and "work file name". Also make sure you populate the tradedata.csv accordingly. You can just paste trade data from ATW runs and place all data below the "Comment" row, then save the tradedata.csv file you've pasted all that information in. Also make sure you don't delete the first row by an chance because it contains all the necessary formulas. Just edit columns to suite your needs but don't delete or edit values in the columns with formulas. That is column: C, D, H, I and P. You can just use ChatGPT to  help you to run this code. Its super easy. Enjoy the project!

You might prefer time being displayed as integers or numericals. So, just experiment with either.

To run the script with the following command:

python time-numericals.py

or

python time-integers.py

You should see data being appended in the following google sheet.

https://docs.google.com/spreadsheets/d/1yHzn560nbGmKAqGGUKkTMPu0Fuj-jnfJBIkz-V0N8zM/edit#gid=0
