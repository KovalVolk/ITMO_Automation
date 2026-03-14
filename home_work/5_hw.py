from selenium import webdriver
from selenium.webdriver.common.by import By


def check_elements('https://saucedemo.com/', username_locator, password_locator, login_locator):


    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")


    username_field = driver.find_element(By.CSS_SELECTOR, '#user-name')

    password_field = driver.find_element(By.CSS_SELECTOR, '#password')

    login_button = driver.find_element(By.CSS_SELECTOR, '#login-button')

    if username_field and  password_field and login_button:
       print('Элементы найдены')
    else:
       print('Элементы не найдены')
