import time
from xmlrpc.client import Boolean
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
serv_obj = Service("/Users/jiniab/Downloads/geckodriver 2")
driver = webdriver.Firefox(service=serv_obj)
driver.get("http://facebook.com")
element = driver.find_element(By.XPATH, " //div[@id='reg_pages_msg']")
print(element.text)
print("The value of the div class is" + element.get_attribute("class"))
# ***********************************checking the web element Email textfield is present or not***************************************
email_text: bool = driver.find_element(By.CSS_SELECTOR, "#email").is_displayed()
if email_text:
    print("Email Textfield is present")
else:
    print('Email textfield is not present')
ele_email = driver.find_element(By.CSS_SELECTOR, "#email")
ele_email.clear()
ele_email.send_keys("adb@gmail.com")
# **********************************checking the web element password textfield is present or not*****************************************
Password_text: bool = driver.find_element(By.CSS_SELECTOR, "input[name='pass']").is_displayed()
if Password_text:
    print("password text field is present")
else:
    print("Password text is not present")

    ele_password = driver.find_element(By.CSS_SELECTOR, "input[name='pass']")
    ele_password.send_keys("star123")
# **********************************checking the web element Button  is present and Enabled  ********************************************
    ele_button_displayed: bool = driver.find_element(By.CSS_SELECTOR, "button[name='login']").is_displayed()
ele_button_enabled: bool = driver.find_element(By.CSS_SELECTOR, "button[name='login']").is_enabled()
if ele_button_enabled == True & ele_button_enabled == True:
    driver.find_element(By.CSS_SELECTOR, "button[name='login']").click()
    print("Logged in successfully")
else:
    print("Login button not working")

driver.close()
