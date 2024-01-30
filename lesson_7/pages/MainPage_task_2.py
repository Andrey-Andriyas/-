from selenium.webdriver.common.by import By

class MainPage:
    
    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def input_delay_time(self, delay_time):
        clear_field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        clear_field.clear()
        clear_field.send_keys(delay_time)

    def click_buttons(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, ".operator.btn.btn-outline-success").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-of-type(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-warning").click()
