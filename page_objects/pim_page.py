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

    def __init__(self, driver):
        self.driver = driver

    def click_pim_menu(self):

        pim_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, self.pim_menu_xpath)
            )
        )

        pim_menu.click()

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