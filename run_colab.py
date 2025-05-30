from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# Set up headless Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Log in to Google
driver.get('https://accounts.google.com/signin')
driver.find_element_by_id('identifierId').send_keys(os.getenv('GOOGLE_EMAIL'))
driver.find_element_by_id('identifierNext').click()
time.sleep(2)
driver.find_element_by_name('password').send_keys(os.getenv('GOOGLE_PASSWORD'))
driver.find_element_by_id('passwordNext').click()
time.sleep(5)

# Open and run the Colab notebook
notebook_url = 'https://colab.research.google.com/github/username/repo/blob/main/notebook.ipynb'
driver.get(notebook_url)
time.sleep(5)
driver.find_element_by_id('runtime-menu-button').click()  # Adjust selector as needed
driver.find_element_by_id('run-all').click()  # Simulate "Run all"
time.sleep(60)  # Wait for execution (adjust based on notebook runtime)

driver.quit()