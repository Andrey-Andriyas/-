import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_shop():
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Андрей")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Андрияс")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("660036")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    txt = driver.find_element(By.CSS_SELECTOR, "div[class='summary_info_label summary_total_label']").text
    driver.quit()
    assert txt == "Total: $58.29"

