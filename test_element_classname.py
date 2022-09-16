import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj = Service("/Users/jiniab/Downloads/chromedriver-3")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://google.com")


elem = driver.find_element(By.PARTIAL_LINK_TEXT, "How Search")
elem.click()

print(driver.current_url)
time.sleep(5)
driver.close()
