import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

final_text = ""
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(final_text)


@pytest.mark.parametrize('page_num', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_collect_hidden_message(browser, page_num):
    global final_text
    # open page
    link = f"https://stepik.org/lesson/236{page_num}/step/1"
    browser.get(link)
    # enter correct answer
    answer = str(math.log(int(time.time())))
    enter_field = WebDriverWait(browser, 15).until(ec.presence_of_element_located((By.CLASS_NAME, "ember-text-area")))
    enter_field.send_keys(answer)
    # push send button
    send_button = browser.find_element(By.CLASS_NAME, "submit-submission")
    send_button.click()
    # wait for the correctness check and gather the reaction text
    feedback_element = WebDriverWait(browser, 15).until(ec.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    feedback_text = feedback_element.text
    # if the text is not 'Correct!' - collect it
    if feedback_text != 'Correct!':
        final_text += feedback_text
