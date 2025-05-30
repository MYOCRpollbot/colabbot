import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
 
    driver.get('https://accounts.google.com')

    # Enter email
    email_field = driver.find_element(By.ID, 'identifierId')
    email_field.send_keys(os.getenv('GOOGLE_EMAIL'))
    driver.find_element(By.ID, 'identifierNext').click()
    time.sleep(2)

    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(os.getenv('GOOGLE_PASSWORD'))
    driver.find_element(By.ID, 'passwordNext').click()
    time.sleep(5)

notebook_url = 'https://colab.research.google.com/drive/1RVnrB1RFtyBSASEBDyQxmLK5OwsHSvu8?usp=drive_link'
driver.get(notebook_url)
time.sleep(5) 
    print("Logged in successfully.")

finally:
    driver.quit()
