from login import login
from selenium.webdriver.common.by import By

import time




def selecting_products(driver):
    product_page = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item']")
    product_list = []

    for product in product_page:
        find_items = product.find_element(By.XPATH, ".//div[@class='inventory_item_name '] ").text
        product_list.append(find_items)

    print(product_list)


    selected_product = []
    select_no_product = int(input("Choose no of product you want add in cart: "))

    for item in range(select_no_product):
        if select_no_product > 6:
            print("Total product is 6")
            break
        elif select_no_product <= 6:
            select_product_add_to_cart = int(input("PRODUCT ARE LISTED IN SERIAL SELECT 1,2,3,4,5,6 TO ADD IN CART: "))
            selected_product.append(product_list[select_product_add_to_cart - 1])
    assert len(selected_product) == select_no_product

    for product in product_page:
        find_items = product.find_element(By.XPATH, ".//div[@class='inventory_item_name '] ").text
        for products in selected_product:
            if find_items == products:
                product.find_element(By.XPATH, ".//button[contains(@id, 'add-to-cart')]").click()
    return selected_product

def opening_cart(driver):
    driver.find_element(By.XPATH, "//a[@class =  'shopping_cart_link']").click()
    time.sleep(2)

    cart_products = []
    price_list = []
    new_cart_item = driver.find_elements(By.XPATH, "//div[@class =  'cart_item']")
    for cart_prod in new_cart_item:
        cart_item = cart_prod.find_element(By.XPATH, ".//div[@class =  'inventory_item_name']").text
        find_price = cart_prod.find_element(By.XPATH, ".//div[@class = 'inventory_item_price']").text
        cart_products.append(cart_item)
        price_list.append(float(find_price.replace("$","")))
    print(cart_products)
    total = sum(price_list)
    print(total)
    return cart_products,total


def checkout():
    driver = login()
    selecting_products(driver)
    cart_open,total  = opening_cart(driver)
    driver.find_element(By.XPATH, "//button[@data-test = 'checkout']").click()
    checkouts = []
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@data-test = 'firstName']").send_keys("ABHISHEK")
    driver.find_element(By.XPATH, "//input[@data-test = 'lastName']").send_keys("PASWAN")
    driver.find_element(By.XPATH, "//input[@data-test = 'postalCode']").send_keys("122001")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@data-test = 'continue']").click()
    time.sleep(1)
    items_in_checkout = driver.find_elements(By.XPATH, "//div[@data-test = 'inventory-item']")
    check_tot = []
    for item in items_in_checkout:
        show_item = item.find_element(By.XPATH, ".//a[@ role = 'button']").text
        checkouts_total = item.find_element(By.XPATH, ".//div[@class = 'inventory_item_price']").text
        checkouts.append(show_item)
        check_tot.append(float(checkouts_total.replace("$","")))
        time.sleep(1)
    check_total_sum = sum(check_tot)
    for product in cart_open:
        assert product in checkouts
    assert len(checkouts) == len(cart_open)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@id = 'finish']").click()
    time.sleep(1)
    successful = driver.find_element(By.XPATH, "//h2[@class = 'complete-header']").text
    assert successful == "Thank you for your order!"
    assert total == check_total_sum


if __name__ == "__main__":
    checkout()
