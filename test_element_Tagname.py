import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj = Service("/Users/jiniab/Downloads/chromedriver-3")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://google.com")
ele1 = driver.find_elements(By.CLASS_NAME, "KxwPGc SSwjIe").__sizeof__()
print(ele1)
ele = driver.find_elements(By.TAG_NAME, "a").__sizeof__()
print(ele)
driver.close()
