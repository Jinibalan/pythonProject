# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

serv_obj = Service("/Users/jiniab/Downloads/geckodriver 2")
driver = webdriver.Firefox(service=serv_obj)
# implicit wait 10 seconds
driver.implicitly_wait(10)
driver.get("http://google.com")
driver.maximize_window()
searchbox = driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
searchbox.submit()
# chances of getting synchronisation problem so error will get no such element
# one method is to do time module.it will reduce the performance and also he element
# is not not visible until the tim mentioned ,still problem of getting errors.
# time.sleep(4) is coming from python.
path = driver.find_element(By.XPATH, "//a/h3[text()='Selenium']")
print(path.text)
path.click()
driver.close()

