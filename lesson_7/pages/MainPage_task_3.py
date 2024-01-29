from selenium.webdriver.common.by import By

class MainPage:
    
    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def input_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    
    def input_password(self):
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()


