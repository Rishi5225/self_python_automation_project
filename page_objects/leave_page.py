from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LeavePage:

    # ---------------- LEFT MENU ----------------

    leave_menu_xpath = "//span[text()='Leave']"

    # ---------------- TOP TABS ----------------

    apply_tab_xpath = "//a[text()='Apply']"

    my_leave_tab_xpath = "//a[text()='My Leave']"

    entitlements_tab_xpath = "//span[text()='Entitlements ']"

    reports_tab_xpath = "//span[text()='Reports ']"

    configure_tab_xpath = "//span[text()='Configure ']"

    leave_list_tab_xpath = "//a[text()='Leave List']"

    assign_leave_tab_xpath = "//a[text()='Assign Leave']"

    # ---------------- ENTITLEMENTS DROPDOWN ----------------

    add_entitlements_xpath = "//a[text()='Add Entitlements']"

    employee_entitlements_xpath = "//a[text()='Employee Entitlements']"

    my_entitlements_xpath = "//a[text()='My Entitlements']"

    # ---------------- REPORTS DROPDOWN ----------------

    leave_entitlements_report_xpath = "//a[text()='Leave Entitlements and Usage Report']"

    my_leave_entitlements_report_xpath = "//a[text()='My Leave Entitlements and Usage Report']"

    # ---------------- CONFIGURE DROPDOWN ----------------

    leave_period_xpath = "//a[text()='Leave Period']"

    leave_types_xpath = "//a[text()='Leave Types']"

    work_week_xpath = "//a[text()='Work Week']"

    holidays_xpath = "//a[text()='Holidays']"

    # ---------------- PAGE HEADERS ----------------

    apply_leave_header_xpath = "//h6[text()='Apply Leave']"

    my_leave_header_xpath = "//h5[text()='My Leave List']"

    leave_list_header_xpath = "//h5[text()='Leave List']"

    assign_leave_header_xpath = "//h6[text()='Assign Leave']"

    # ---------------- CONSTRUCTOR ----------------

    def __init__(self, driver):

        self.driver = driver

    # ---------------- GENERIC CLICK ----------------

    def click_element(self, xpath):

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, xpath)
            )
        ).click()

    # ---------------- GENERIC VALIDATION ----------------

    def validate_element_visible(self, xpath):

        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, xpath)
            )
        ).is_displayed()