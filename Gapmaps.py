from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from urllib.parse import urljoin
import os
import requests
import time
# Create a user agent object
#user_agent = UserAgent()

# Define your desired user agent string
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.54"

# Create Edge options object
options = Options()

# Set the user agent string
options.add_argument(f"user-agent={user_agent}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Create the driver with the options
driver = webdriver.Edge(options=options)

# Get a random user agent string
#random_user_agent = user_agent.random

# Specify the URL and path to Chrome driver
url = "https://live.gapmaps.com/login"


# Select a directory to save the images

download_dir = "/path/to/download/directory"

# Create a new Chrome driver instance
#driver = webdriver.Chrome(chromedriver_path)
#driver = webdriver.Edge(executable_path="./msedgedriver.exe")
#driver = webdriver.Edge(EdgeChromiumDriverManager().install())
service = Service(r"C:\Users\r14ale\Desktop\Gapmaps\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Navigate to the specified URL
driver.get(url)
#driver.implicitly_wait(10)

driver.implicitly_wait(500)
# Locate email and password fields
# Locate the element by ID
password_field = driver.find_element(By.ID, "password-label")
password_field = password_field.click()
#password_field.send_keys("JermaineCheah123!")
# email_field = driver.find_element(By.ID, "email")
# email_field = email_field.click()
# email_field.send_keys("johnson.goh@zuscoffee.com")
# password_field = driver.find_element(By.ID, "password").click()
# password_field.send_keys("JermaineCheah123!")

# Enter email and password
# email_field.send_keys("johnson.goh@zuscoffee.com")
# password_field.send_keys("JermaineCheah123!")

# # Wait for the page to load
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# # Find all images on the page
# images = driver.find_elements_by_tag_name("img")

# # Extract the image URLs
# image_urls = [image.get_attribute("src") for image in images]

# # Download the images
# for image_url in image_urls:
#     # Create the full image URL
#     full_image_url = urljoin(url, image_url)

#     # Extract the image filename
#     filename = os.path.basename(image_url)

#     # Download the image
#     with open(os.path.join(download_dir, filename), "wb") as f:
#         driver.get(full_image_url)
#         image_data = driver.find_element_by_tag_name("img").get_attribute("src")
#         f.write(requests.get(image_data).content)

# # Close the driver
# driver.quit()

# print("Images downloaded successfully!")