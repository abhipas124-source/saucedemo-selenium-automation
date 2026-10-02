import time

from login import login
from selenium.webdriver.common.by import By




def dynamic_product_add_to_cart():
    driver = login()
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
            selected_product.append(product_list[select_product_add_to_cart-1])
    assert len(selected_product) == select_no_product

    for product in product_page:
        find_items = product.find_element(By.XPATH, ".//div[@class='inventory_item_name '] ").text
        for products in selected_product:
            if find_items == products:
                product.find_element(By.XPATH, ".//button[contains(@id, 'add-to-cart')]").click()


    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@class =  'shopping_cart_link']").click()
    time.sleep(2)

    cart_products =[]
    new_cart_item = driver.find_elements(By.XPATH, "//div[@class =  'cart_item']")
    for cart_prod in new_cart_item:
        cart_item = cart_prod.find_element(By.XPATH, ".//div[@class =  'inventory_item_name']").text
        cart_products.append(cart_item)
    print(cart_products)
    assert len(cart_products) == len(selected_product)


    list_to_remove = []
    to_remove_product =int(input("select number of product to remove: "))
    for cart_prods in range(to_remove_product):
        if to_remove_product <= len(cart_products):
            select_product_remove_from_cart = int(input("SELECT product TO REMOVE FROM CART: "))
            list_to_remove.append(cart_products[select_product_remove_from_cart-1])

    for cart_prod in new_cart_item:
        cart_item = cart_prod.find_element(By.XPATH, ".//div[@class =  'inventory_item_name']").text
        for re_items in list_to_remove:
            if cart_item == re_items:
                cart_prod.find_element(By.XPATH, ".//button[contains(@id,  'remove' )]").click()

    remaining_products=[]
    remaining_cart_item = driver.find_elements(By.XPATH, "//div[@class =  'cart_item']")
    for remaining_prod in remaining_cart_item:
        cart_item = remaining_prod.find_element(By.XPATH, ".//div[@class =  'inventory_item_name']").text
        remaining_products.append(cart_item)
    for product in list_to_remove:
        assert product not in remaining_products

if __name__ == "__main__":
    dynamic_product_add_to_cart()