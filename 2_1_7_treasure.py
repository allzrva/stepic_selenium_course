import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(from_x):
    return str(math.log(abs(12*math.sin(int(from_x)))))


browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    # time.sleep(5) # sometimes the browser is not fast enough to load the page
    # find x and calculate y = calc(x)
    print('page loaded')
    x_element = browser.find_element(By.ID, "treasure")
    print('element found')
    x = x_element.get_attribute("valuex")
    print(f'x is {x}')
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
    time.sleep(15)
    # close session
    browser.quit()
