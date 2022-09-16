
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="/Users/jiniab/Downloads/chromedriver-3")
driver.get("http://itera-qa.azurewebsites.net/home/automation")
radio_btn = driver.find_element(By.ID, "female")
radio_btn.click()
print(radio_btn.text)
status = radio_btn.is_selected()
print(status)
