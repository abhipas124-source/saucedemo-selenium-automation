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
                time.sleep(1)
                products_in_list = {"Name": name,"Price": price}

                list1.append(products_in_list)
    return list1

def cart_price(driver):

    list2 = []
    driver.find_element(By.XPATH, "//a[@data-test = 'shopping-cart-link']").click()
    time.sleep(1)
    cart_product_detail = driver.find_elements(By.XPATH, "//div[@class = 'cart_item']")
    for cart_product in cart_product_detail:
        name = cart_product.find_element(By.XPATH, ".//div[@data-test = 'inventory-item-name']").text
        price_in_str = cart_product.find_element(By.XPATH, ".//div[@data-test = 'inventory-item-price']").text
        price = float(price_in_str.replace("$",""))
        cart_product_process = {"Name": name, "Price":price}
        list2.append(cart_product_process)
    return list2

def check_out():
    driver = login()
    initial_products_overview = selected_products(driver)
    carts_price = cart_price(driver)
    list3 = []
    driver.find_element(By.XPATH, "//button[@id = 'checkout']").click()
    driver.find_elements(By.XPATH, "//div[@class = 'checkout_info']")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@id = 'first-name']").send_keys("Abhishek")
    driver.find_element(By.XPATH,"//input[@id = 'last-name']").send_keys("Paswan")
    driver.find_element(By.XPATH, "//input[@id = 'postal-code']").send_keys("122001")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id = 'continue']").click()
    over_view = driver.find_elements(By.XPATH, "//div[@class = 'cart_item']")
    for over_view_item in over_view:
        name = over_view_item.find_element(By.XPATH, ".//div[@class = 'inventory_item_name']").text
        price_in_str = over_view_item.find_element(By.XPATH, ".//div[@class = 'inventory_item_price']").text
        price = float(price_in_str.replace("$", ""))
        products_in_over_view = {"Name":name, "Price":price}
        list3.append(products_in_over_view)
        for initial_product in initial_products_overview:
            for cart_items in list3:
                if  initial_product["Name"] == cart_items["Name"]:
                    assert initial_product["Price"] == cart_items["Price"]
        for initial_product in initial_products_overview:
            for items in carts_price:
                if initial_product["Name"]==items["Name"]:
                    assert initial_product["Price"] == items["Price"]
        for items in carts_price:
                for cart_items in list3:
                    if cart_items["Name"]==items["Name"]:
                        assert items["Price"] == cart_items["Price"]


if __name__ == "__main__":
    check_out()