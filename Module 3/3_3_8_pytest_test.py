from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# run this test case from terminal with command 'pytest 3_3_8_pytest_test.py'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def test_positive_test_case():
    browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe', options=options)
    try:
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        welcome_text = verify_registration(browser)
        assert welcome_text == "Congratulations! You have successfully registered!",\
            f"Expected text: Congratulations! You have successfully registered!, Actual text: {welcome_text}"
    finally:
        browser.quit()


def test_negative_test_case():
    browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe', options=options)
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        welcome_text = verify_registration(browser)
        assert welcome_text == "Congratulations! You have successfully registered!",\
            f"Expected text: Congratulations! You have successfully registered!, Actual text: {welcome_text}"
    finally:
        browser.quit()


def verify_registration(browser):
    # fill names and e-mail
    browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('John')
    browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Doe')
    browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('john.d@mailbox.com')
    # submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(2)
    return browser.find_element(By.TAG_NAME, "h1").text
