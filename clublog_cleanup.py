'''
1. Install Python 3 into C:\Python3. If pronpted to add Python to PATH, say YES.
2. Create a folder C:\selenium
3. Downbload Chromedriver from https://chromedriver.chromium.org/downloads. It must be the version that corresponds to your version of Chrome
4. Unzip Chromedriver.exe and put it in to C:\Python3
5. Go to Command (CMD) in WIndows
6. type "pip install -U selenium". This will install Selenium for Python
7. Change variables CALLSIGN and CLUBLOGPASSWORD to your credentials 
7. Amend this script below to set the start and end date ranges in the 6 fields (startyear/month/day/endyear/month/day)
8. Then run this script in python by going to CMD and typing "python clublog_python.py" and pressing enter
'''

# Make Selenium available to Python
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


def mainloop(STARTYEAR,STARTMONTH,STARTDAY,ENDYEAR,ENDMONTH,ENDDAY):
  # go to the filter page and fill it in
  driver.get("https://clublog.org/inspector.php")

  #set start year, month and day
  # year
  select = Select(driver.find_element(By.ID,"startyear"))
  select.select_by_visible_text(STARTYEAR)
  #select.select_by_index(1)
  #select.select_by_value('2019')

  # month
  select = Select(driver.find_element(By.ID,"startmonth"))
  select.select_by_visible_text(STARTMONTH)
  #select.select_by_index(10)
  #select.select_by_value('11')

  # day
  select = Select(driver.find_element(By.ID,"startday"))
  select.select_by_visible_text(STARTDAY)
  #select.select_by_index(10)
  #select.select_by_value('11')

  # set end year, month and day
  select = Select(driver.find_element(By.NAME,"endyear"))
  select.select_by_visible_text(ENDYEAR)

  # month
  select = Select(driver.find_element(By.NAME,"endmonth"))
  select.select_by_visible_text(ENDMONTH)

  # day
  select = Select(driver.find_element(By.NAME,"endday"))
  select.select_by_visible_text(ENDDAY)

  # click Search
  driver.find_element(By.NAME, "test").click()

  # check if delete button is present on the page. 
  # If yes, click the X.
  # If not, end the browser session as there are no records to delete
  try:
    driver.find_element(By.ID,"del1")
    print("Delete button found - yay!")
    driver.find_element(By.ID,"del1").click() # click X
    mainloop()
  except:
    print("No Delete button found")
    driver.quit()


# Set the constants
CALLSIGN = "your callsign"
CLUBLOGPASSWORD = "yourpassword"
STARTYEAR = "2020"
STARTMONTH = "7"
STARTDAY = "15"
ENDYEAR = "2020"
ENDMONTH = "7"
ENDDAY = "15"

# Open a Chrome session. Relies on Chromedriver to be installed somewhere where PATH can see it
driver = webdriver.Chrome() 
driver.maximize_window()

# Open the web page on the login screen
driver.get("https://clublog.org/loginform.php") 

# Find the username field by ID and send a value
driver.find_element(By.ID, "fEmail").send_keys(CALLSIGN)

# Find the password field byID and send a value
driver.find_element(By.NAME, "fPassword").send_keys(CLUBLOGPASSWORD) 

# Find the Submit button and click it
driver.find_element(By.ID, "submit").click()

# run the script
mainloop(STARTYEAR,STARTMONTH,STARTDAY,ENDYEAR,ENDMONTH,ENDDAY)