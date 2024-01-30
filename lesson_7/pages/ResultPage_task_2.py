from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:

    def __init__(self, browser):
        self.driver = browser

    def get_result(self):
        waiter = WebDriverWait(self.driver, 46, 0.01).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text