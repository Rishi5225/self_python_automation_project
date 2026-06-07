from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LeavePage:

    # ---------------- LEFT MENU ----------------

    leave_menu_xpath = "//span[normalize-space()='Leave']"

    # ---------------- TOP TABS ----------------

    apply_tab_xpath = "//a[normalize-space()='Apply']"

    my_leave_tab_xpath = "//a[normalize-space()='My Leave']"

    entitlements_tab_xpath = "//span[normalize-space()='Entitlements']"

    reports_tab_xpath = "//span[normalize-space()='Reports']"

    configure_tab_xpath = "//span[normalize-space()='Configure']"

    leave_list_tab_xpath = "//a[normalize-space()='Leave List']"

    assign_leave_tab_xpath = "//a[normalize-space()='Assign Leave']"

    # ---------------- ENTITLEMENTS DROPDOWN ----------------

    add_entitlements_xpath = "//a[normalize-space()='Add Entitlements']"

    employee_entitlements_xpath = "//a[normalize-space()='Employee Entitlements']"

    my_entitlements_xpath = "//a[normalize-space()='My Entitlements']"

    # ---------------- REPORTS DROPDOWN ----------------

    leave_entitlements_report_xpath = "//a[contains(.,'Leave Entitlements and Usage Report')]"

    my_leave_entitlements_report_xpath = "//a[contains(.,'My Leave Entitlements and Usage Report')]"

    # ---------------- CONFIGURE DROPDOWN ----------------

    leave_period_xpath = "//a[normalize-space()='Leave Period']"

    leave_types_xpath = "//a[normalize-space()='Leave Types']"

    work_week_xpath = "//a[normalize-space()='Work Week']"

    holidays_xpath = "//a[normalize-space()='Holidays']"

    # ---------------- PAGE HEADERS ----------------

    apply_leave_header_xpath = "//h6[normalize-space()='Apply Leave']"

    my_leave_header_xpath = "//h5[normalize-space()='My Leave List']"

    leave_list_header_xpath = "//h5[normalize-space()='Leave List']"

    assign_leave_header_xpath = "//h6[normalize-space()='Assign Leave']"

    # ---------------- CONSTRUCTOR ----------------

    def __init__(self, driver):

        self.driver = driver

    # ---------------- GENERIC CLICK ----------------

    def click_element(self, xpath):

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, xpath)
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of(element)
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    # ---------------- GENERIC VALIDATION ----------------

    def validate_element_visible(self, xpath):

        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, xpath)
            )
        )

        return element.is_displayed()

