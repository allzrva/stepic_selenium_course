import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

expected_link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
try:
    browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
    browser.get(link)

    found_link = browser.find_element(By.LINK_TEXT, expected_link_text)
    found_link.click()

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Sascha")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("E")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Nizhny Novgorod")
    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, ".button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
