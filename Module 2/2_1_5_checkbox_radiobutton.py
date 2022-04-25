import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(from_x):
    return str(math.log(abs(12*math.sin(int(from_x)))))


browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
try:
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    # find x and calculate y = calc(x)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # enter y
    browser.find_element(By.ID, 'answer').send_keys(y)

    # Check 'i'm the robot' checkbox and push the 'Robots rule' button
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()

    # Submit answer
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # wait time to see the answer code
    time.sleep(20)
    # close session
    browser.quit()
