from faker import Faker
from page_objects.pim_page import PIMPage


class TestPIM:
    
    fake = Faker()

    def test_add_employee(self, login_setup):

        self.driver = login_setup

        pim = PIMPage(self.driver)

        pim.click_pim_menu()

        pim.click_add_employee()

        first_name = self.fake.first_name()
        last_name = self.fake.last_name()

        pim.enter_first_name(first_name)

        pim.enter_last_name(last_name)

        pim.click_save()

        assert pim.validate_personal_details_header()


class TestPIMConfiguration:

    def test_configuration_dropdown_validation(self, login_setup):

        self.driver = login_setup

        pim = PIMPage(self.driver)

        pim.click_pim_menu()

        pim.click_configuration_menu()

        assert pim.validate_optional_fields()

        assert pim.validate_custom_fields()

        assert pim.validate_data_import()

        assert pim.validate_reporting_methods()

        assert pim.validate_termination_reasons()


class TestPIMOptionalFields:

    def test_optional_fields_toggle_validation(self, login_setup):

        self.driver = login_setup

        pim = PIMPage(self.driver)

        pim.click_pim_menu()

        pim.click_configuration_menu()

        pim.click_optional_fields()

        pim.turn_on_all_toggles()

        pim.turn_off_all_toggles()

        pim.click_save_button()