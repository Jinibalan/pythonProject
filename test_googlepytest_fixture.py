from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("--------------SetUp-----------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")

    yield
    print("--------------tear Down------------")
    driver.quit()


def test_google_title(init_driver):
    assert driver.title == "Google"


def test_google_url(init_driver):
    assert driver.current_url == "http://www.google.com/?gws_rd=ssl"
