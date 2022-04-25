import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, 'input')
    for index, element in enumerate(elements):
        element.send_keys("TeHehe")
        print(f'filled in the element {index+1}')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
