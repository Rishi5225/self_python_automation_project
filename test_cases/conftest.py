import pytest
#from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium import webdriver


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

    
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
