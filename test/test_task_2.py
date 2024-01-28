from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_slow_calculator():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.implicitly_wait(4)
    driver.maximize_window()
    delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay.clear()
    delay.send_keys("45")
    button_7 = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary").click()
    button_plus = driver.find_element(By.CSS_SELECTOR, ".operator.btn.btn-outline-success").click()
    button_8 = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-of-type(2)").click()
    button_equal = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-warning").click()
    
    waiter = WebDriverWait(driver, 46, 0.01).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
    
    assert driver.find_element(By.CSS_SELECTOR, '.screen').text == "15"

    driver.quit()