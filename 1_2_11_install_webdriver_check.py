from selenium import webdriver

# инициализируем драйвер браузера.
# После этой команды вы должны увидеть новое открытое окно браузера 'C:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome('C:\\chromedriver\\chromedriver.exe')
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://stepik.org/lesson/25969/step/12")
# Ищем поле для ввода текста.так как у меня грузится слишком медленно, код валится.
textarea = driver.find_element_by_css_selector(".textarea")
# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
# Найдем кнопку
submit_button = driver.find_element_by_css_selector(".submit-submission")
# нажать на кнопку
submit_button.click()
# закрыть окно браузера
driver.quit()
