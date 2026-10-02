from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
assert "Swag Labs" in driver.title
enter_username = (driver.find_element(By.XPATH, "//input[@id='user-name']"))
enter_username.send_keys("standard_user")
enter_password = driver.find_element(By.XPATH, "//input[@id='password'] ")
enter_password.send_keys("secret_sauce")
enter_password.send_keys(Keys.RETURN)
time.sleep(3)

to_find_the_product = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item']")
time.sleep(3)

product_list_name = []
integer_price = []
product_list_price = []
for items in to_find_the_product:
    product_name = items.find_element(By.XPATH, ".//div[@class= 'inventory_item_name ']").text
    product_list_name.append(product_name)

    product_price = items.find_element(By.XPATH, ".//div[@class= 'inventory_item_price']").text
    product_list_price.append(product_price)

    product_details = {"name": product_name,
                       "price": product_price}
    integer_price.append(product_details)


for products in integer_price:
    products["price"] = float(products["price"].replace("$",""))
cheapest = min(integer_price, key=lambda product : product["price"])
print(cheapest)
