from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


from pages.MainPage_task_1 import MainPage
from pages.ResultPage_task_1 import ResultPage

def test_form_elements():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    main_page = MainPage(browser)
    main_page.input_first_name("Иван")
    main_page.input_last_name("Петров")
    main_page.input_name_address("Ленина, 55-3")
    main_page.input_name_email("test@skypro.com")
    main_page.input_name_phone("+7985899998787")
    main_page.input_zip_code("")
    main_page.input_name_city("Москва")
    main_page.input_name_country("Россия")
    main_page.input_name_job_position("QA")
    main_page.input_name_company("SkyPro")
    main_page.push_submit(browser)

    result_page = ResultPage(browser)
    
    assert result_page.background_color_zip_code(browser) == "rgba(248, 215, 218, 1)"
    assert result_page.background_color_other_fields(browser) == "rgba(209, 231, 221, 1)"

    browser.quit()