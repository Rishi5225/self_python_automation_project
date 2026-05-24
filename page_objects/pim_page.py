from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PIMPage:

    add_employee_button_xpath = "//a[text()='Add Employee']"

    first_name_xpath = "//input[@name='firstName']"

    last_name_xpath = "//input[@name='lastName']"

    save_button_xpath = "//button[@type='submit']"

    personal_details_header_xpath = "//h6[text()='Personal Details']"

    pim_menu_xpath = "//span[text()='PIM']"

    configuration_menu_xpath = "//span[@class='oxd-topbar-body-nav-tab-item' and contains(text(), 'Configuration')]"
    optional_fields_xpath = "//a[contains(text(), 'Optional Fields')]"
    custom_fields_xpath = "//a[contains(text(), 'Custom Fields')]"
    data_import_xpath = "//a[contains(text(), 'Data Import')]"
    reporting_methods_xpath = "//a[contains(text(), 'Reporting Methods')]"
    termination_reasons_xpath = "//a[contains(text(), 'Termination Reasons')]"

    nickname_toggle_xpath = "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]"

    ssn_toggle_xpath = "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[2]"
    sin_toggle_xpath = "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[3]"
    tax_toggle_xpath = "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[4]"
    all_toggle_buttons_xpath = "//span[contains(@class,'oxd-switch-input')]"
    save_button_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def click_pim_menu(self):

        pim_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.pim_menu_xpath)
            )
        )

        pim_menu.click()
        
        # Wait for menu to load after click
        import time
        time.sleep(2)

    def click_add_employee(self):

        add_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.add_employee_button_xpath)
            )
        )

        add_btn.click()

    def enter_first_name(self, first_name):

        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, self.first_name_xpath)
            )
        )

        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):

        last_name_field = self.driver.find_element(
            By.XPATH,
            self.last_name_xpath
        )

        last_name_field.send_keys(last_name)

    def click_save(self):

        self.driver.find_element(
            By.XPATH,
            self.save_button_xpath
        ).click()
        
        # Wait for page to load after save
        import time
        time.sleep(2)

    def validate_personal_details_header(self):

        return WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(
                (By.XPATH, self.personal_details_header_xpath)
            )
        ).is_displayed()

    def click_configuration_menu(self):

        # Note: XPath may need to be updated based on actual page structure
        # The Configuration menu might appear as a dropdown or submenu item
        config_menu = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.configuration_menu_xpath)
            )
        )

        config_menu.click()
        
        # Wait for configuration menu to load
        import time
        time.sleep(2)

    def validate_optional_fields(self):

        optional_fields = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, self.optional_fields_xpath)
            )
        )

        return optional_fields.is_displayed()

    def validate_custom_fields(self):

        custom_fields = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, self.custom_fields_xpath)
            )
        )

        return custom_fields.is_displayed()

    def validate_data_import(self):

        data_import = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, self.data_import_xpath)
            )
        )

        return data_import.is_displayed()

    def validate_reporting_methods(self):

        reporting_methods = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, self.reporting_methods_xpath)
            )
        )

        return reporting_methods.is_displayed()

    def validate_termination_reasons(self):

        termination_reasons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, self.termination_reasons_xpath)
            )
        )

        return termination_reasons.is_displayed()

    def click_optional_fields(self):

        optional_fields = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.optional_fields_xpath)
            )
        )

        optional_fields.click()


    def get_all_toggle_buttons(self):

        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, self.all_toggle_buttons_xpath)
            )
        )


    def turn_on_all_toggles(self):

        toggle_buttons = self.get_all_toggle_buttons()

        for toggle in toggle_buttons:

            if "oxd-switch-input--active" not in toggle.get_attribute("class"):

                toggle.click()


    def turn_off_all_toggles(self):

        toggle_buttons = self.get_all_toggle_buttons()

        for toggle in toggle_buttons:

            if "oxd-switch-input--active" in toggle.get_attribute("class"):

                toggle.click()


    def click_save_button(self):

        save_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.save_button_xpath)
            )
        )

        save_btn.click()