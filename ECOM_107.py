import time
from login import login
from selenium.webdriver.common.by import By


def inventory_item():
    driver = login()
    selected_item = search()
    if selected_item is None:
        driver.quit()
        return
    product_page = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item']")


    for product in product_page:
        find_items = product.find_element(By.XPATH, ".//div[@class='inventory_item_name '] ").text
       #print(find_items)
        if find_items == selected_item:
            add_to_cart=product.find_element(By.XPATH, ".//button[contains(@id, 'add-to-cart')]")
            add_to_cart.click()
            #print("True")
            break
        time.sleep(2)
    driver.find_element(By.XPATH, "//a[@class =  'shopping_cart_link']").click()
    time.sleep(2)
    cart_item = driver.find_element(By.XPATH, "//div[@class =  'inventory_item_name']").text

    assert selected_item==cart_item
    print("TRUE")

    driver.quit()
def search():
    item = int(input("chooise: 1,2,3: \n"))
    if item == 1:
        return "Sauce Labs Backpack"
    elif item == 2:
        return  "Sauce Labs Bike Light"
    elif item == 3:
        return  "Sauce Labs Bolt T-Shirt"
    else:
        print("item not found")
        return  None

if __name__ == "__main__":
    inventory_item()