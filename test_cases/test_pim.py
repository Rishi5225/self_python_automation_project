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