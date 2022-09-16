
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dc = DesiredCapabilities.CHROME
dc['goog:loggingPrefs'] = {'browser': 'ALL'}
driver = webdriver.Chrome(executable_path="/Users/jiniab/Downloads/chromedriver-3", desired_capabilities=dc)
driver.get("https://www.google.com")
for e in driver.get_log('browser'):
    print(str(e))
driver.quit()
