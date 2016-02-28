from selenium import webdriver #needed to start up accessing the webpages
from selenium.webdriver.common.keys import Keys #used for sending text and keyboard keys to web page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #selenium's webdriver expected conditions
from selenium.webdriver.common.by import By
import getpass #hide password from echoing to terminal when run from commandline

emailToSearch = input('Please enter in the email: ')
password = getpass.getpass()
driver = webdriver.Chrome("C:\Python34\Scripts\chromedriver.exe")
driver.get('https://mail.google.com/')


elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "Email")))   
driver.find_element_by_id("Email")
elem.send_keys(str(emailToSearch))
driver.find_element_by_id("next").click()
elem2=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "Passwd")))    
elem2.send_keys(str(password))
driver.find_element_by_id("signIn").click()
assert "Not a valid email." not in driver.page_source
