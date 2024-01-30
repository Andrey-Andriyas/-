from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.FormPage_task_1 import FormPage


def test_form_elements():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    form_page = FormPage(browser)
    form_page.input_field("first-name", "Иван")
    form_page.input_field("last-name", "Петров")
    form_page.input_field("address", "Ленина, 55-3")
    form_page.input_field("e-mail", "test@skypro.com")
    form_page.input_field("phone", "+7985899998787")
    form_page.input_field("zip-code", "")
    form_page.input_field("city", "Москва")
    form_page.input_field("country", "Россия")
    form_page.input_field("job-position", "QA")
    form_page.input_field("company", "SkyPro")
    form_page.click_submit_button()

    field_colors = form_page.get_field_background_colors()

    assert field_colors[5] == "rgba(248, 215, 218, 1)"
    assert all(color == "rgba(209, 231, 221, 1)" for color in field_colors[:5] + field_colors[6:])

    browser.quit()