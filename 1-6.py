from selenium import webdriver
from selenium.webdriver.common.by import By
#from faker import Faker
import time

#fake = Faker("ru_RU")

link = "http://suninjuly.github.io/registration1.html"
# link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #  заполняем обязательные поля
    #fio = fake.name().split()
    # email = fake.ascii_free_email()
    fio = "Пупкин Вася Батькович".split()
    email = "e@mail.ru"
    browser.find_element(By.CSS_SELECTOR,'input.first[required]').send_keys(fio[1])
    browser.find_element(By.CSS_SELECTOR,'input.second[required]').send_keys(fio[0])
    browser.find_element(By.CSS_SELECTOR,'input.third[required]').send_keys(email)
    # browser.find_element(By.CSS_SELECTOR,'input[placeholder="Input your phone:"]').send_keys(fake.phone_number())
    # browser.find_element(By.CSS_SELECTOR,'input[placeholder="Input your address:"]').send_keys(fake.address())

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
