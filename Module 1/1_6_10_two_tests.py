from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
try:
    # link = "http://suninjuly.github.io/registration1.html"  # link to pass
    link = "http://suninjuly.github.io/registration2.html" # link to fail
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('John')
    browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Doe')
    browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('john.d@mailbox.com')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
