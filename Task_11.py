import time
from selenium.webdriver.common.by import By
from login import login

def selected_products(driver):

    list1 = []
    product_details = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item']")
    product = ["Sauce Labs Bolt T-Shirt","Sauce Labs Backpack","Sauce Labs Bike Light"]
    for select_product in product_details:
        name = select_product.find_element(By.XPATH, ".//div[@class = 'inventory_item_name ']").text
        price_in_str = select_product.find_element(By.XPATH, ".//div[@class = 'inventory_item_price']").text
        price =float(price_in_str.replace("$",""))
        for products in product:
            if name==products:
                select_product.find_element(By.XPATH, ".//button[contains(@id, 'add-to-cart')]").click()
                products_in_list = {"Name": name,"Price": price}

                list1.append(products_in_list)
    return list1,product

def Cart_price():
    driver = login()
    list2 = []
    initial_products,shopping_page_products_detail = selected_products(driver)
    driver.find_element(By.XPATH, "//a[@data-test = 'shopping-cart-link']").click()
    cart_product_detail = driver.find_elements(By.XPATH, "//div[@class = 'cart_item']")
    for cart_product in cart_product_detail:
        name = cart_product.find_element(By.XPATH, ".//div[@data-test = 'inventory-item-name']").text
        price_in_str = cart_product.find_element(By.XPATH, ".//div[@data-test = 'inventory-item-price']").text
        price = float(price_in_str.replace("$",""))
        cart_product_process = {"Name": name, "Price":price}
        list2.append(cart_product_process)

    for initial_product in initial_products:
        for items in list2:
            if initial_product["Name"] == items["Name"]:
                assert initial_product["Price"] == items["Price"]


if __name__ == "__main__":
    Cart_price()