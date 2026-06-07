
# import pytest
# import undetected_chromedriver as uc
# from selenium import webdriver

# from page_objects.login import Login
# from utilities.read_properties import ReadConfigProperties


# # ------------------------------
# # Add command line browser option
# # ------------------------------
# def pytest_addoption(parser):
#     parser.addoption("--browser")


# # ------------------------------
# # Browser fixture
# # ------------------------------
# @pytest.fixture()
# def set_up(request):

#     browser = request.config.getoption("--browser")

#     if browser == "chrome":
#         driver = uc.Chrome()

#     elif browser == "firefox":
#         driver = webdriver.Firefox()

#     else:
#         driver = uc.Chrome()

#     driver.maximize_window()
#     driver.implicitly_wait(10)

#     yield driver

#     driver.quit()


# # ------------------------------
# # Login fixture (BDD Background)
# # ------------------------------
# @pytest.fixture()
# def login_setup(set_up):

#     driver = set_up

#     driver.get(ReadConfigProperties.get_url())
    
#     # Wait for the page to load completely
#     import time
#     time.sleep(3)

#     login = Login(driver)

#     login.set_username(ReadConfigProperties.get_username())
#     login.set_password(ReadConfigProperties.get_password())
#     login.click_login()
    
#     # Wait for dashboard to load completely
#     WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "oxd-topbar"))
#     )
    
#     time.sleep(2)

#     return driver


import pytest
import undetected_chromedriver as uc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.login import Login
from utilities.read_properties import ReadConfigProperties


# ---------------------------------
# Hook for test result status
# ---------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


# ---------------------------------
# Add command line options
# ---------------------------------
def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode"
    )


# ---------------------------------
# Browser fixture
# ---------------------------------
@pytest.fixture(scope="class")
def set_up(request):

    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    # ---------------- CHROME ----------------
    if browser == "chrome":

        options = uc.ChromeOptions()

        # Headless mode
        if headless:
            options.add_argument("--headless=new")

        # CI/CD & Docker compatible options
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")

        driver = uc.Chrome(options=options)

    # ---------------- FIREFOX ----------------
    elif browser == "firefox":

        firefox_options = webdriver.FirefoxOptions()

        if headless:
            firefox_options.add_argument("--headless")

        driver = webdriver.Firefox(options=firefox_options)

    # ---------------- DEFAULT ----------------
    else:

        options = uc.ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")

        driver = uc.Chrome(options=options)

    try:
        driver.maximize_window()
    except Exception:
        try:
            driver.set_window_size(1920,1080)
        except Exception:
            pass

    driver.implicitly_wait(10)

    print("Browser launched successfully")

    yield driver

    # ---------------------------------
    # Screenshot on failure
    # ---------------------------------
    # if request.node.rep_call.failed:

    #     screenshot_path = f"screenshots/{request.node.name}.png"

    #     driver.save_screenshot(screenshot_path)

    #     print(f"Screenshot saved at: {screenshot_path}")

    # driver.delete_all_cookies()
    # driver.quit()

    # print("Browser closed successfully")

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        import os

        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = f"screenshots/{request.node.name}.png"

        driver.save_screenshot(screenshot_path)

        print(f"Screenshot saved at: {screenshot_path}")

    driver.delete_all_cookies()
    driver.quit()

    print("Browser closed successfully")


# ---------------------------------
# Login fixture
# ---------------------------------
@pytest.fixture(scope="class")
def login_setup(set_up):

    driver = set_up

    driver.get(ReadConfigProperties.get_url())

    login = Login(driver)

    login.set_username(ReadConfigProperties.get_username())
    login.set_password(ReadConfigProperties.get_password())
    login.click_login()

    # Explicit wait for dashboard
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "oxd-topbar"))
    )

    print("Login successful")

    return driver
