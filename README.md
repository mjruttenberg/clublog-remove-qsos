# clublog-remove-qsos

Clublog is a website where amateur radio ethunsiasts can upload their logs.
Sometimes a user has more than 1 callsign, and it sometimes happens that a user can upload a log against the wrong callsign.

The aim of this script is to enable a user to log in to clublog.org and remove QSOs (ham radio contacts) that have been uploaded against a particular callsign.

Requires:
Python3
Selenium Webdriver
Chromedriver, added to a path that is accessible by the system PATH

The execution steps are:
1. Log in to the site using your callsign
2. Go to the Log Inspector page
3. Select a date range (start and end date year, month and day for each)
4a. If there are any rows returned, click the X (delete) button, which returns the user to step 2
4b. If there are no rows returned, close the session

TO DO (maybe):
* Move the credentials to an ENV file
* check that the credentials are valid (check that the user doesn't get the credentials failed screen), if failed then loop back to ask for credentials
* ask the user to input the date ranges from a picker/dropdown
* when a valid date range is entered,  show the user the results and prompt them to accept before proceeding with the deletion
* back up the existing data before deleting any data
