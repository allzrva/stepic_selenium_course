from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


class Test3_2_13(unittest.TestCase):
    def test_positive_test_case(self):
        browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe', options=options)
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser.get(link)
            welcome_text = self.verify_registration(browser)
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                             f"Expected text: Congratulations! You have successfully registered!, Actual text: {welcome_text}")
        finally:
            time.sleep(2)
            browser.quit()

    def test_negative_test_case(self):
        browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe', options=options)
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser.get(link)
            welcome_text = self.verify_registration(browser)
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                             f"Expected text: Congratulations! You have successfully registered!, Actual text: {welcome_text}")
        finally:
            time.sleep(2)
            browser.quit()

    @staticmethod
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


if __name__ == "__main__":
    unittest.main()
