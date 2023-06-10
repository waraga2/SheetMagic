# SheetMagic
SheetMagic: A Python script that magically appends data from a CSV file to a Google Sheets document.


#About This Project

This Python script reads data from a CSV file and appends it to a Google Sheet.


#Installation

This project can be run by installing a few pip dependencies by running the following commands.

pip install gspread oauth2client

Then git clone this repo.

Download your own json key file from google cloud console by following these steps laid out in the following article (its quite lengthy to have it all here), start reading the part where it says "Create a Json Key File" to save yourself some time==> 

https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/

Alternatively, you could use my json key file provided in this repo, for demonstration purposes only. I have provided you with an excellent google sheet, if you run the python script you'll directly be appending data to that spreadsheet. And you'll see data being appended there. If you want to utilise this python script on your own projects, which is why i beleive you're here. You should make a copy of the spreadsheet provided. Rename the copy of that spreadsheet. And then in the python script specify you worksheet name, the sheet file name, and edit the json keyfile path and place your own json keyfile path there (Hopefully it wasn't much of hustle to obtain your keyfile as demonstrated in the article provided). And DO NOT DELETE THE FIRST OR THE SECOND ROW of the sheetfile, you a can only edit the figures in the SECOND row. However be cautious when editing the SECOND ROW, there are array formulas in column C, D, H, I and, P these help in computing results for those respective columns. So if you wanted to edit those array formulas for those columns in order to fit your needs, you need to take that array formula and paste it into ChatGPT and ask it to make it compute in the way you want. For example the array formula for that calculates the Target Profit multiplies the stake by 3, you can easily edit the 3 out and put in the number you want so that it corresponds to the Target Profit you want. Also make sure you populate the tradedata.csv accordingly. You can just copy and paste trade data from the Auto Trader Web, (and obviously this script is made holistically for this very purpose). Once you've copied the data generated from a single run, paste it below the "Comment" section in the tradedata.csv file. Save the CSV file, and then run the time-numericals.py script. All data in the CSV file will be appended to sheet file. Voila!

Again, be careful don't edit the names of the columns in the First Row, since you'd be required to also make the same changes in the python script. Data in the Second  Row can be edited out, but you have to make sure you're careful with the array formulas. All the rest of the rows from the third row and on, can be deleted and be messed around however you wish. the The script takes around 50 secs to fully append all the data to a given row, so give it some allowance when running.
 

To run the script with the following command:

python time-numericals.py

You should see data being appended in the following google sheet if you've not put in your own json key file path or edited the script for your own personal use. Enjoy!

https://docs.google.com/spreadsheets/d/1yHzn560nbGmKAqGGUKkTMPu0Fuj-jnfJBIkz-V0N8zM/edit#gid=0
