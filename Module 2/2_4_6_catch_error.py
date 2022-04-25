from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
try:
    link = "http://suninjuly.github.io/cats.html"
    browser.get(link)

    browser.find_element(By.ID, "button")
except NoSuchElementException as e:
    print(f'you may have a problem: {e}')

finally:
    # close session
    browser.quit()
