from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Google Chrome
driver_1 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_1.maximize_window()
driver_1.get("http://the-internet.herokuapp.com/add_remove_elements/")
for x in range(0, 5):
    push_element = driver_1.find_element(By.CSS_SELECTOR, "button")
    push_element.send_keys(Keys.RETURN)
button_delete = driver_1.find_elements(By.CSS_SELECTOR, "button.added-manually")
print(len(button_delete))

#Mozilla FireFox
# driver_2 = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# driver_2.maximize_window()
# driver_2.get("http://the-internet.herokuapp.com/add_remove_elements/")

# for x in range(0, 5):
#     push_element = driver_2.find_element(By.CSS_SELECTOR, "button")
#     push_element.send_keys(Keys.RETURN)
# button_delete = driver_2.find_elements(By.CSS_SELECTOR, "button.added-manually")
# print(len(button_delete))

sleep(5)