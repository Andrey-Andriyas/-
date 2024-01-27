import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def open_bonigarcia():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(4)
    driver.maximize_window()

def forms_filling():
    first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    address = driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    phone_number = driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    zip_code = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").clear()
    city = driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    country = driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    company = driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

def click_submit():
    driver.find_element(By.CSS_SELECTOR, "button").click()

def test_zip_code_element():
    open_bonigarcia()
    forms_filling()
    click_submit()
    assert driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color") == "rgba(248, 215, 218, 1)"

def test_first_name_element():
    open_bonigarcia()
    forms_filling()
    click_submit()
    assert driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"

def test_last_name_element():
    open_bonigarcia()
    forms_filling()
    click_submit()
    assert driver.find_element(By.CSS_SELECTOR, "#last-name").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"

def test_address_element():
    open_bonigarcia()
    forms_filling()
    click_submit()
    assert driver.find_element(By.CSS_SELECTOR, "#address").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"

def test_email_element():
    open_bonigarcia()
    forms_filling()
    click_submit()
    assert driver.find_element(By.CSS_SELECTOR, "#e-mail").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"

def test_phone_number_element():
    open_bonigarcia()
    forms_filling()
    click_submit()
    assert driver.find_element(By.CSS_SELECTOR, "#phone").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"

def test_city_element():
    open_bonigarcia()
    forms_filling()
    click_submit()
    assert driver.find_element(By.CSS_SELECTOR, "#city").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"

def test_country_element():
    open_bonigarcia()
    forms_filling()
    click_submit()
    assert driver.find_element(By.CSS_SELECTOR, "#country").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"

def test_job_position_element():
    open_bonigarcia()
    forms_filling()
    click_submit()
    assert driver.find_element(By.CSS_SELECTOR, "#job-position").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"

def test_company_element():
    open_bonigarcia()
    forms_filling()
    click_submit()
    assert driver.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"

    driver.quit()