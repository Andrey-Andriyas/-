from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


from pages.MainPage_task_2 import MainPage
from pages.ResultPage_task_2 import ResultPage


def test_slow_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    main_page.input_delay_time("45")
    main_page.click_buttons()

    result_page = ResultPage(browser)

    assert result_page.get_result() == "15"

    browser.quit()