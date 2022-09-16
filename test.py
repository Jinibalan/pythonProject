from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/jiniab/Downloads/chromedriver-3")

driver.get("http://newtours.demoat.com/")
print(driver.title)  # Title of the page
driver.close()        # close the browser

