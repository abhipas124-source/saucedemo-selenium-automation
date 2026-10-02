from login import login
from selenium.webdriver.common.by import By

def products_ask(driver):


    to_find_the_product = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item']")

    previous_price = []
    integer_price = []

    for items in to_find_the_product:
        price_of_products_ws = items.find_element(By.XPATH, ".//div[@class= 'inventory_item_price']").text
        product = {"price": price_of_products_ws}
        previous_price.append(product)
    for products in previous_price:
        products["price"] = float(products["price"].replace("$",""))
        integer_price.append(products)

    return previous_price