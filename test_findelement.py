import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/jiniab/Downloads/chromedriver-3")
driver.get("https://wiki.ubuntu.com")
print(driver.title)
ele = driver.find_element(By.ID, "searchinput")
ele.send_keys('facebook')
time.sleep(5)
driver.close()

