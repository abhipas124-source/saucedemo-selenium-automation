from selenium.webdriver.common.by import By
import time


def sorted_product(driver):

    driver.find_element(By.XPATH, "//select[@aria-label= 'Sort products']").click()
    driver.find_element(By.XPATH, "//option[@value= 'lohi']").click()
    time.sleep(2)

    new_to_find_the_product = driver.find_elements(By.XPATH, "//div[@class = 'inventory_item']")

    list1 = []
    list2 = []
    for i in new_to_find_the_product:
        new_search = i.find_element(By.XPATH, ".//div[@class= 'inventory_item_price']").text
        new_i_value = {"new_price": new_search}
        list1.append(new_i_value)
    for j in list1:
        j["new_price"] = float(j["new_price"].replace("$", ""))
        list2.append(j)
    return list1


