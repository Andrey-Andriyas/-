from selenium.webdriver.common.by import By

class MainPage:
    
    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()


    def input_first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(first_name)

    def input_last_name(self, last_name):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(last_name)

    def input_name_address(self, name_address):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(name_address)

    def input_name_email(self, name_email):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(name_email)

    def input_name_phone(self, name_phone):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(name_phone)
    
    def input_zip_code(self, zip_code):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys(zip_code)

    def input_name_city(self, name_city):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(name_city)

    def input_name_country(self, name_country):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(name_country)

    def input_name_job_position(self, name_job_position):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(name_job_position)

    def input_name_company(self, name_company):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(name_company)

    def push_submit(self, browser):
        self.driver.find_element(By.CSS_SELECTOR, "button").click()