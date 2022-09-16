import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium.webdriver.firefox.service import Service

serv_obj = Service("/Users/jiniab/Downloads/geckodriver 2")

driver = webdriver.Firefox(service=serv_obj)
driver.get("https://facebook.com")
ele_email = driver.find_element(By.CSS_SELECTOR, "#email")
ele_Pass = driver.find_element(By.CSS_SELECTOR, "input[name='pass']")
print(ele_email.get_attribute("type"))
print(ele_Pass.get_attribute("type"))
ele_email.send_keys("abcs@gmial.com")
ele_Pass.send_keys("star123*")
driver.find_element(By.CSS_SELECTOR, "button[name='login']").click()
print("testing finished")
time.sleep(4)
driver.close()
