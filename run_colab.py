import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

print("Setting up Chrome options...")
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080") # Set window size for headless

print("Initializing Chrome driver...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20) # Increased wait time

try:
    print("Navigating to Google login page...")
    driver.get("https://accounts.google.com")

    # Enter email
    print("Entering email...")
    email_field = wait.until(EC.visibility_of_element_located((By.ID, "identifierId")))
    email_field.send_keys(os.getenv("GOOGLE_EMAIL"))
    driver.find_element(By.ID, "identifierNext").click()
    # time.sleep(2) # Replaced with WebDriverWait

    # Enter password
    print("Entering password...")
    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd"))) # Corrected element name based on common Google login flow
    password_field.send_keys(os.getenv("GOOGLE_PASSWORD"))
    driver.find_element(By.ID, "passwordNext").click()
    # time.sleep(5) # Replaced with WebDriverWait, wait for next page element if possible
    print("Login submitted. Waiting for potential 2FA or redirect...")
    # Add a wait condition here if you know what element appears after successful login
    # For example: wait.until(EC.url_contains("myaccount.google.com"))
    # Or just a fixed wait if the next step doesn't depend on a specific element
    time.sleep(10) # Increased sleep after login attempt, adjust as needed

    print("Login attempt finished. Navigating to Colab notebook...")
    notebook_url = "https://colab.research.google.com/drive/1RVnrB1RFtyBSASEBDyQxmLK5OwsHSvu8?usp=drive_link"
    driver.get(notebook_url)
    print(f"Attempting to load notebook: {notebook_url}")
    # Wait for a specific element in Colab to ensure it loaded
    # Example: wait.until(EC.presence_of_element_located((By.ID, "connect")))
    print("Waiting for Colab notebook page elements...")
    time.sleep(15) # Increased sleep for Colab load, adjust as needed
    print("Successfully navigated to Colab notebook URL (page load assumed complete).")

except Exception as e:
    print(f"An error occurred: {e}")
    # Optional: Capture screenshot on error
    # driver.save_screenshot("error_screenshot.png")

finally:
    print("Closing the browser.")
    driver.quit()

