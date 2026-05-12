from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    admin_menu_xpath = "//span[text()='Admin']"
    pim_menu_xpath = "//span[text()='PIM']"
    leave_menu_xpath = "//span[text()='Leave']"
    time_menu_xpath = "//span[text()='Time']"
    recruitment_menu_xpath = "//span[text()='Recruitment']"
    myinfo_menu_xpath = "//span[text()='My Info']"
    performance_menu_xpath = "//span[text()='Performance']"
    dashboard_menu_xpath = "//span[text()='Dashboard']"
    directory_menu_xpath = "//span[text()='Directory']"
    maintenance_menu_xpath = "//span[text()='Maintenance']"
    claim_menu_xpath = "//span[text()='Claim']"
    buzz_menu_xpath = "//span[text()='Buzz']"

    def __init__(self, driver):
        self.driver = driver

    def validate_element(self, locator):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, locator)
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

        return element.is_displayed()

    def validate_admin_menu(self):
        return self.validate_element(self.admin_menu_xpath)

    def validate_pim_menu(self):
        return self.validate_element(self.pim_menu_xpath)

    def validate_leave_menu(self):
        return self.validate_element(self.leave_menu_xpath)

    def validate_time_menu(self):
        return self.validate_element(self.time_menu_xpath)

    def validate_recruitment_menu(self):
        return self.validate_element(self.recruitment_menu_xpath)

    def validate_myinfo_menu(self):
        return self.validate_element(self.myinfo_menu_xpath)

    def validate_performance_menu(self):
        return self.validate_element(self.performance_menu_xpath)

    def validate_dashboard_menu(self):
        return self.validate_element(self.dashboard_menu_xpath)

    def validate_directory_menu(self):
        return self.validate_element(self.directory_menu_xpath)

    def validate_maintenance_menu(self):
        return self.validate_element(self.maintenance_menu_xpath)

    def validate_claim_menu(self):
        return self.validate_element(self.claim_menu_xpath)
    
    def validate_buzz_menu(self):
        return self.validate_element(self.buzz_menu_xpath)
    
