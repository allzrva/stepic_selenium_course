import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(from_x):
    return str(math.log(abs(12*math.sin(int(from_x)))))


browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # click to go on a magical journey
    browser.find_element(By.CLASS_NAME, "btn").click()

    # switch to another tab
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    # calculate math
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # submit answer
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    # wait time to see the answer code
    time.sleep(10)
    browser.switch_to.alert.accept()
    # close session
    browser.quit()
