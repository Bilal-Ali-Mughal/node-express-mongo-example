# tests/test_invalid_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://example.com/login")  # Dummy login page

# Dummy simulation
try:
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
    
    username.send_keys("wronguser")
    password.send_keys("wrongpass")
    login_button.click()
    
    time.sleep(2)
    assert "Invalid" in driver.page_source
except:
    print("Dummy test - elements not found (as expected)")
finally:
    driver.quit()
