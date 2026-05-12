
from selenium.webdriver.common.by import By


class TestDashboard:

    def test_dashboard_title(self, login_setup):

        self.driver = login_setup

        assert self.driver.title == "OrangeHRM"

    def test_dashboard_header(self, login_setup):

        self.driver = login_setup

        dashboard = self.driver.find_element(
            By.XPATH,
            "//h6[text()='Dashboard']"
        ).text

        assert dashboard == "Dashboard"