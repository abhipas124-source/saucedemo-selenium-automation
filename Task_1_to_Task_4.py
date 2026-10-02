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

to_find_the_product = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item_name ']")

for items in to_find_the_product:
    print(items.text)
print(f"Total products = {len(to_find_the_product)}")
assert len(to_find_the_product) > 0