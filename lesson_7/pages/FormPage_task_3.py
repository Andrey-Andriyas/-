from selenium.webdriver.common.by import By

class FormPage:

    def __init__(self, browser):
        self.driver = browser
    
    def input_first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(first_name)

    def input_last_name(self, last_name):
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(last_name)

    def input_postal_code(self, postal_code):
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(postal_code)
    
    def click_continue(self):
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()





