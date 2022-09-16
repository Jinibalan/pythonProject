from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
serv_obj = Service("/Users/jiniab/Downloads/chromedriver-3")
driver = webdriver.Chrome(service=serv_obj)
driver.get("http://itera-qa.azurewebsites.net/home/automation")
element_dropdown = driver.find_element(By.XPATH, "//select[@class='custom-select']")
select = Select(element_dropdown)
# select By visible text
select.select_by_visible_text('Greece')
select.select_by_index(7)
