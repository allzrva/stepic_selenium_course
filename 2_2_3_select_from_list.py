import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
try:
    #link = "http://suninjuly.github.io/selects1.html"
    link = "http://suninjuly.github.io/selects2.html"
    browser.get(link)
    print('finished loading')

    # get two numbers and calculate their sum
    val1 = int(browser.find_element(By.ID, "num1").text)
    val2 = int(browser.find_element(By.ID, "num2").text)
    val_sum = val1 + val2
    print(f'sum is {val_sum}')

    # select the correct answer
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(val_sum))

    # submit the answer
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # wait time to see the answer code
    time.sleep(15)
    # close session
    browser.quit()
