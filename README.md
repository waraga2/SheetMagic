# SheetMagic
SheetMagic is a Python script that enables you to magically append data from a CSV file to a Google Sheets document.


#About This Project

This Python script is designed to read data from a CSV file and append it to a Google Sheet effortlessly.

#Installation

To run this project, you need to install the required dependencies using pip. Run the following command:

pip install gspread oauth2client

After installing the dependencies, clone this repository to your local machine.

Next, you need to obtain a JSON key file from the Google Cloud Console. Follow the steps outlined in this article here to download your own JSON key file. Skip to the section titled "Create a JSON Key File" for instructions on obtaining the key file.

https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/

Alternatively, for demonstration purposes, you can use the JSON key file provided in this repository. By running the Python script, you will directly append data to the provided Google Sheet. If you intend to use this script for your own projects, make a copy of the provided spreadsheet, rename it, and specify the worksheet name and sheet file name in the Python script. Additionally, update the path of the JSON key file with your own file path (assuming you obtained your own key file as described in the aforementioned article).

Important: Do not delete the first or second row of the sheet file. You can only edit the figures in the second row. Exercise caution when modifying the second row since there are array formulas in columns C, D, H, I, and P that compute results for those respective columns. If you need to edit these array formulas, copy the formula and ask ChatGPT to compute it according to your requirements. For example, the array formula that calculates the Target Profit multiplies the stake by 3. You can modify the number to correspond to your desired Target Profit.

Ensure that you populate the tradedata.csv file correctly. You can copy and paste trade data from the Auto Trader Web (as this script is specifically designed for this purpose). After copying the data generated from a single run, paste it below the "Comment" section in the tradedata.csv file. Save the CSV file and then execute the time-numericals.py script. All data in the CSV file will be appended to the sheet file. Voila!

Again, be careful not to edit the names of the columns in the first row, as you would need to make the corresponding changes in the Python script as well. The data in the second row can be modified, but exercise caution with the array formulas. Rows from the third row onwards can be deleted or modified as desired. The script takes approximately 50 seconds to fully append all the data to the specified row, so please allow sufficient time when running it.

# To execute the script, use the following command:

python time-numericals.py

If you have not provided your own JSON key file path or made any changes to the script for your personal use, you should see the data being appended to the following Google Sheet. Enjoy!

#Google Sheet Link
https://docs.google.com/spreadsheets/d/1yHzn560nbGmKAqGGUKkTMPu0Fuj-jnfJBIkz-V0N8zM/edit#gid=0
