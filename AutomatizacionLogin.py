from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

username = "problem_user"
password = "secret_sauce"

url = "https://www.saucedemo.com/"

driver = webdriver.Chrome("C:/Users/YADIRA/PycharmProjects/pythonProject/chromedriver")

driver.get(url)
driver.maximize_window()
sleep(5)
driver.find_element(By.ID,"user-name").send_keys(username)
sleep(5)
driver.find_element(By.NAME,"password").send_keys(password)
sleep(5)
driver.find_element(By.ID, "login-button").click()

print("Inicio de sesión correcto")

driver.quit()
