import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def calc(from_x):
    return str(math.log(abs(12*math.sin(int(from_x)))))


browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # wait till 15 seconds until the price of house is 100
    button = WebDriverWait(browser, 15).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    # calculate math
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # submit answer
    browser.find_element(By.ID, "answer").send_keys(y)
    submit_btn = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_btn)
    submit_btn.click()

finally:
    # wait time to see the answer code
    time.sleep(10)
    browser.switch_to.alert.accept()
    # close session
    browser.quit()
