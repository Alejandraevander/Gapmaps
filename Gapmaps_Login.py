from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

web = "https://live.gapmaps.com/login"
path = r"C:\Users\r14ale\Desktop\Gapmaps\\msedgedriver.exe"

#https://stackoverflow.com/questions/76377363/how-can-i-disable-personalize-your-web-experience-ms-edge-prompt-for-selenium
#Compulsory Code in Selenium 4.0
options = webdriver.EdgeOptions()
service = Service(path)

#Code to Disable the Devtools listening on ....
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.add_argument("--headless=new")
options.add_argument("--guest")
options.add_argument("windows-size=1920x1080")

#Open MS Edge webdriver and opening the website
driver = webdriver.Edge(service=service, options=options)
driver.get(web)

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"password")))

#Login Details
password_field = driver.find_element(By.XPATH, "//input[@name='password']")
password_field.click()
time.sleep(5)
password_field.send_keys(os.environ.get('PASSWORD'))

email_field = driver.find_element(By.XPATH, "//input[@id='email']")
email_field.click()
time.sleep(5)
email_field.send_keys(os.environ.get('EMAIL'))

#Login Button
button = driver.find_element(By.ID, "submit-login")
button.click()
time.sleep(30)
#driver.maximize_window()
#Close website
driver.quit()