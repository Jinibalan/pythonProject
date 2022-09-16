import time
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
service_obj = Service("/Users/jiniab/Downloads/chromedriver-3")
driver = webdriver.Chrome(service=service_obj)
# explicit wait function
# wait = WebDriverWait(driver, 10)
wait = WebDriverWait(driver, 10, ignored_exceptions=[exceptions])
driver.get("http://google.com")
driver.maximize_window()
searchbox = driver.find_element(By.NAME, "q")
searchbox.send_keys("Selenium")
searchbox.submit()
searchLink = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
searchLink.click()
