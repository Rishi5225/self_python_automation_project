# import pytest
# #from selenium.webdriver.chrome.options import Options
# import undetected_chromedriver as uc
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# options = uc.ChromeOptions()

# @pytest.fixture()
# def set_up(browser):
#     if browser == "chrome":
#         driver = uc.Chrome()

#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         driver = uc.Chrome()
#     driver.maximize_window()
#     driver.implicitly_wait(10)  # Add implicit wait

    
#     return driver

# def pytest_addoption(parser):
#     parser.addoption("--browser")

# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

import pytest
import undetected_chromedriver as uc
from selenium import webdriver

from page_objects.login import Login
from utilities.read_properties import ReadConfigProperties


# ------------------------------
# Add command line browser option
# ------------------------------
def pytest_addoption(parser):
    parser.addoption("--browser")


# ------------------------------
# Browser fixture
# ------------------------------
@pytest.fixture()
def set_up(request):

    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = uc.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        driver = uc.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# ------------------------------
# Login fixture (BDD Background)
# ------------------------------
@pytest.fixture()
def login_setup(set_up):

    driver = set_up

    driver.get(ReadConfigProperties.get_url())

    login = Login(driver)

    login.set_username(ReadConfigProperties.get_username())
    login.set_password(ReadConfigProperties.get_password())
    login.click_login()

    return driver
