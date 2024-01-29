from selenium.webdriver.common.by import By

class ResultPage:

    def __init__(self, browser):
        self.driver = browser
    
    def total_cost(self):
        txt = self.driver.find_element(By.CSS_SELECTOR, "div[class='summary_info_label summary_total_label']").text
        return(txt)