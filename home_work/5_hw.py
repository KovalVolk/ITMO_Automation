from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://saucedemo.com/")

#Поиск элемента
icon = driver.find_element(By.CSS_SELECTOR, id = "user-name")
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

icon1 = driver.find_element(By.CSS_SELECTOR, id = "password")
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

icon2 = driver.find_element(By.CSS_SELECTOR, id = "login-button")
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')
