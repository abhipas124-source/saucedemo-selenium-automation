from tkinter.constants import COMMAND

from click import command
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
assert "Swag Labs" in driver.title
time.sleep(2)

enter_username = (driver.find_element(By.XPATH, "//input[@id='user-name']"))
time.sleep(2)

enter_username.send_keys("standard_user")
time.sleep(2)

enter_password = driver.find_element(By.XPATH, "//input[@id='password'] ")
time.sleep(2)

enter_password.send_keys("secret_sauce")
time.sleep(2)

enter_password.send_keys(Keys.RETURN)
time.sleep(2)

menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
time.sleep(3)

logout = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
logout.click()
time.sleep(2)

username = driver.find_element(By.XPATH, "//input[@id='user-name']")
username.send_keys("secret_sauce")
time.sleep(2)

login_click = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_click.click()
time.sleep(2)
assert driver.find_element(By.XPATH, "//h3[@data-test='error']").text == "Epic sadface: Password is required"
username.send_keys(Keys.COMMAND ,"a")
username.send_keys(Keys.BACKSPACE)
time.sleep(2)

dismiss_button = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss error']")
dismiss_button.click()
time.sleep(2)

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("09876")
time.sleep(2)

login_again_click = driver.find_element(By.XPATH, "//input[@id='login-button']")
login_again_click.click()
time.sleep(2)

assert driver.find_element(By.XPATH, "//h3[@data-test='error']").text == "Epic sadface: Username is required"
login_again_click.send_keys(Keys.COMMAND ,"a")
login_again_click.send_keys(Keys.BACKSPACE)
time.sleep(2)

dismiss_button = driver.find_element(By.XPATH, "//button[@aria-label='Dismiss error']")
dismiss_button.click()
time.sleep(2)
print("true")
time.sleep(1)

driver.close()
