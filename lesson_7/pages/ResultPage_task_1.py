from selenium.webdriver.common.by import By

class ResultPage:

    def __init__(self, browser):
        self.driver = browser

    def background_color_zip_code(self, browser):
        zip_code_color = self.driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
        return zip_code_color

    def background_color_other_fields(self, browser):
        other_fields = ["#first-name", "#last-name", "#address", "#e-mail", "#phone", "#city", "#country", "#job-position", "#company"]
        for field in other_fields:
            field_color = self.driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color")
        return field_color