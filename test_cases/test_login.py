from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfigProperties
from page_objects.login import Login
import time


class TestLoginPage:
    base_url = ReadConfigProperties.get_url()
    username = ReadConfigProperties.get_username()
    password = ReadConfigProperties.get_password()

    def test_login_page_title(self,set_up):
        self.driver = set_up
        self.driver.get(self.base_url)
        time.sleep(10)

        page_title = self.driver.title

        if page_title == "OrangeHRM":
            self.driver.close()
            assert True
        
        else:
            self.driver.save_screenshot(r"F:\\self_python_automation_project\\screen_shots\\failed.png")
            assert False

    def test_login(self,set_up):
        self.driver = set_up
        self.driver.get(self.base_url)

        self.login_pg_obj = Login(self.driver)
        self.login_pg_obj.set_username(self.username)
        self.login_pg_obj.set_password(self.password)
        self.login_pg_obj.click_login()
        time.sleep(10)

        page_title = self.driver.title

        if page_title == "OrangeHRM":
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot(r"F:\\self_python_automation_project\\screen_shots\\failed.png")
            self.driver.close()
            assert False