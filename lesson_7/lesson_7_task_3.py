from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from pages.MainPage_task_3 import MainPage
from pages.ProductsPage_task_3 import ProductsPage
from pages.CartPage_task_3 import CartPage
from pages.FormPage_task_3 import FormPage
from pages.ResultPage_task_3 import ResultPage

def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    main_page = MainPage(browser)
    main_page.input_login()
    main_page.input_password()
    main_page.click_login_button()

    products_page = ProductsPage(browser)
    products_page.add_products()

    cart_page = CartPage(browser)
    cart_page.click_checkout()

    form_page = FormPage(browser)
    form_page.input_first_name("Андрей")
    form_page.input_last_name("Андрияс")
    form_page.input_postal_code("660036")
    form_page.click_continue()

    result_page = ResultPage(browser)

    assert result_page.total_cost() == "Total: $58.29"

    browser.quit()
