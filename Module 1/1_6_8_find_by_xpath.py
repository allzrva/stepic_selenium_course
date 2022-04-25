import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
input_data = ['Sasha', 'E', 'Nizhny Novgorod', 'Roissja']
try:
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, 'input')
    if not elements:
        print('found no elements to fill in')
    for index, element in enumerate(elements):
        element.send_keys(input_data[index])
        print(f'Filled element {index}')

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
print('turn off')
