from selenium.webdriver.common.by import By

class FormPage:

    def __init__(self, browser):
        self.driver = browser
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def input_field(self, field_name, value):
        self.driver.find_element(By.CSS_SELECTOR, f"input[name='{field_name}']").send_keys(value)

    def click_submit_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "button").click()

    def get_field_background_colors(self):
        fields = [
            "first-name", "last-name", "address", 
            "e-mail", "phone", "zip-code", 
            "city", "country", "job-position", 
            "company"
        ]
        field_colors = []
        for field in fields:
            field_color = self.driver.find_element(By.CSS_SELECTOR, f"#{field}").value_of_css_property("background-color")
            field_colors.append(field_color)
        return field_colors