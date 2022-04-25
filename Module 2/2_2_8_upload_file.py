import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

current_dir = os.path.abspath(os.path.dirname(__file__))
input_file = os.path.join(current_dir, 'short_bio.txt')
browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
try:
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]').send_keys("John")
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]').send_keys("Doe")
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]').send_keys("john.doe@mailbox.com")
    browser.find_element(By.ID, 'file').send_keys(input_file)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # wait time to see the answer code
    time.sleep(20)
    # close session
    browser.quit()
