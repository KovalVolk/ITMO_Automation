from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://saucedemo.com/")

#Поиск элемента
icon = driver.find_element(By.CSS_SELECTOR, '#user-name')
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

icon1 = driver.find_element(By.CSS_SELECTOR, '#password')
if icon is None:
    print('Элемент не найден')
else:
    print('Элемент найден')

btn = driver.find_element(By.CSS_SELECTOR, '#login-button')
if btn is None:
    print('Элемент не найден')
else:
    print('Элемент найден')
