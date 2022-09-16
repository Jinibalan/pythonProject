
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path="/Users/jiniab/Downloads/geckodriver 2")
driver.implicitly_wait(10)
driver.get("http://www.w3schools.com/html/tryit.asp?filename=tryhtml_links_w3schools")
# driver.find_element(By.TAG_NAME, 'iframe')
# driver.switch_to.frame('iframeResult')
frame_element = driver.find_element(By.ID, "iframeResult")
driver.switch_to.frame(frame_element)
# driver.switch_to.frame(2)
# driver.find_element(By.CSS_SELECTOR, "a[href='https://www.w3schools.com/']").click()
driver.find_element(By.LINK_TEXT, "Visit W3Schools.com!").click()
driver.switch_to.default_content()
driver.find_element(By.ID, 'getwebsitebtn').click()
driver.close()
