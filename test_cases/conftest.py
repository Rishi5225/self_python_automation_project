
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
    
    # Wait for the page to load completely
    import time
    time.sleep(3)

    login = Login(driver)

    login.set_username(ReadConfigProperties.get_username())
    login.set_password(ReadConfigProperties.get_password())
    login.click_login()
    
    # Wait for login to complete
    time.sleep(3)

    return driver
