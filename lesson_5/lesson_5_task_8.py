from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#GoogleChrome
driver_1 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_1.maximize_window()
driver_1.get("http://the-internet.herokuapp.com/login")
sleep(3)
input_username = driver_1.find_element(By.CSS_SELECTOR, "#username")
sleep(3)
input_username.send_keys("tomsmith")
input_password = driver_1.find_element(By.CSS_SELECTOR, "#password")
sleep(3)
input_password.send_keys("SuperSecretPassword!")
login_button = driver_1.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()



#Mozilla FireFox
# driver_2 = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# driver_2.maximize_window()
# driver_2.get("http://the-internet.herokuapp.com/login")
# sleep(3)
# input_username = driver_2.find_element(By.CSS_SELECTOR, "#username")
# sleep(3)
# input_username.send_keys("tomsmith")
# input_password = driver_2.find_element(By.CSS_SELECTOR, "#password")
# sleep(3)
# input_password.send_keys("SuperSecretPassword!")
# login_button = driver_2.find_element(By.CSS_SELECTOR, "button.radius")
# login_button.click()

sleep(5)