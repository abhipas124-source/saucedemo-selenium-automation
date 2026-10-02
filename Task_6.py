from login import login
from sorted_product import sorted_product
from Sort_function import merge_sort
from product_page import products_ask


def task_6():
    driver = login()
    product_in_new = sorted_product(driver)
    product_in_use = products_ask(driver)
    previous_prices = [
        product["price"]
        for product in product_in_use
    ]
    old_value = merge_sort(previous_prices)
    
    list1 = [
        product["new_price"]
        for product in product_in_new
    ]
    new_value = list1
    assert old_value == new_value, (
        f"Expected: {old_value}, Actual: {new_value}"
    )
    driver.quit()
if __name__ == "__main__":
    task_6()