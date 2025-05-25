# tests/test_page_load.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")  # Dummy page
assert "Example Domain" in driver.title
driver.quit()
