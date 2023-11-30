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
password_field.send_keys("JermaineCheah123!")

email_field = driver.find_element(By.XPATH, "//input[@id='email']")
email_field.click()
time.sleep(5)
email_field.send_keys("johnson.goh@zuscoffee.com")

#Login Button
button = driver.find_element(By.ID, "submit-login")
button.click()
time.sleep(30)
Content = driver.find_element(By.XPATH, "//div[@class='mdc-drawer__content']")
Layers = Content.find_element(By.XPATH, '//button[@aria-label="Layers"]')
Layers.click()
time.sleep(10)
Layers_Section = driver.find_element(By.XPATH, "//Section[@class='nested-drawer s1xqslih']")
B1_precints = Layers_Section.find_element(By.XPATH, "//*[text() = 'B1 Precincts']") 
#B1_precints = driver.find_element(By.LINK_TEXT, 'B1 Precincts')
B1_precints.click()
time.sleep(5)
Major_1 = driver.find_element(By.XPATH, '//input[@id="toggle--Major Retail Precincts - Malaysia"]')
Major_1.click()
time.sleep(5)
Major_2 = driver.find_element(By.XPATH, '//input[@id="toggle--Major Retail Precincts - Malaysia_pins"]')
Major_2.click()
time.sleep(5)
A1_precints = driver.find_element(By.XPATH, "//*[text() = 'A1 Population']")
A1_precints.click()
time.sleep(5)
Mukim_2021 = driver.find_element(By.XPATH, '//input[@id="toggle--3. Mukim - 2021"]')
Mukim_2021.click()
time.sleep(5)
Back_button = driver.find_element(By.XPATH, "//button[@dir='ltr' and @role='button']")
Back_button.click()
time.sleep(5)
Search = driver.find_element(By.XPATH, "//input[@placeholder='Search Location']")
Search.click()
time.sleep(5)

data_keywords = pd.read_csv(r"C:\Users\r14ale\Desktop\Gapmaps\NOF\NF\LCT.csv", encoding="ISO-8859-1", engine='python')
read_keywords = data_keywords['formatted_address']

for keyword in read_keywords:
    Search.send_keys(" ")
    time.sleep(5)
    Search.send_keys(Keys.RETURN)
    time.sleep(5)
    Search.click()
    time.sleep(5)
    Search.send_keys(keyword)
    time.sleep(5)
    Listed = driver.find_element(By.XPATH,"//ul[@role='listbox']")
    time.sleep(5)
    Item = Listed.find_element(By.XPATH, "//li[@id='react-autowhatever-1--item-0' and @data-suggestion-index='0']")
    time.sleep(5)
    Item.click()
#driver.maximize_window()
#Close website
driver.quit()