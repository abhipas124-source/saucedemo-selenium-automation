import time
from login import login
from selenium.webdriver.common.by import By


def inventory_item():
    driver = login()
    cart_products = []
    Multiple_items = ["Sauce Labs Backpack","Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt"]
    product_page = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item']")

    for product in product_page:
        find_items = product.find_element(By.XPATH, ".//div[@class='inventory_item_name '] ").text
        for multi_item in Multiple_items:
            if find_items == multi_item:
                add_to_cart=product.find_element(By.XPATH, ".//button[contains(@id, 'add-to-cart')]")
                add_to_cart.click()
                #print("True")
                break

    driver.find_element(By.XPATH, "//a[@class =  'shopping_cart_link']").click()
    time.sleep(2)
    not_found = []
    new_cart_item = driver.find_elements(By.XPATH, "//div[@class =  'cart_item']")
    for cart_prod in new_cart_item:
        cart_item = cart_prod.find_element(By.XPATH, ".//div[@class =  'inventory_item_name']").text
        cart_products.append(cart_item)
    assert len(cart_products) == len(Multiple_items)
    print("TRUE")
    assert cart_products == Multiple_items
    print("TRUE")
    if multi_item not in cart_products:
        not_found.append(multi_item)
    assert not_found == [], f'not_found_item: {not_found}'
    print("true")

    driver.quit()



if __name__ == "__main__":
    inventory_item()