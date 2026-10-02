from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
def login():
    options = webdriver.ChromeOptions()

    options.add_argument("--incognito")

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "autofill.profile_enabled": False,
            "autofill.credit_card_enabled": False,
        }
    )

    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    assert "Swag Labs" in driver.title

    enter_username = driver.find_element(By.XPATH, "//input[@id='user-name']")
    enter_username.send_keys("standard_user")

    enter_password = driver.find_element(By.XPATH, "//input[@id='password'] ")
    enter_password.send_keys("secret_sauce")
    enter_password.send_keys(Keys.RETURN)
    time.sleep(3)
    return driver