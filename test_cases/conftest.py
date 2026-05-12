import pytest
#from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = uc.ChromeOptions()

@pytest.fixture()
def set_up(browser):
    if browser == "chrome":
        driver = uc.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = uc.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)  # Add implicit wait

    
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
