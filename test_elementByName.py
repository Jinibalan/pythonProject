import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
serv_obj = Service("/Users/jiniab/Downloads/chromedriver-3")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://wiki.ubuntu.com")
ele = driver.find_element(By.ID, "searchinput")
print(ele.text)
ele.send_keys('community')
ele1 = driver.find_element(By.NAME, 'titlesearch')
ele1.click()
time.sleep(5)
driver.close()
