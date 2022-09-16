import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
serv_obj = Service("/Users/jiniab/Downloads/geckodriver 2")
driver = webdriver.Firefox(service=serv_obj)
driver.get("http://itera-qa.azurewebsites.net/home/automation")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print("number of checkboxes in the page are ----")
print(len(checkboxes))
# select multiple checkboxes
for checkbox in checkboxes:
    Name_of_week = checkbox.get_attribute('id')
    if Name_of_week == 'monday' or Name_of_week == 'friday':
        checkbox.click()
    time.sleep(4)
# Deselect the checkbox
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
