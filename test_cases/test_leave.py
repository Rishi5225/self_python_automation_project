from page_objects.leave_page import LeavePage


class TestLeavePage:

    def test_leave_tabs_validation(self, login_setup):

        self.driver = login_setup

        leave = LeavePage(self.driver)

        # Click Leave Menu
        leave.click_element(leave.leave_menu_xpath)

        # Validate Top Tabs

        assert leave.validate_element_visible(
            leave.apply_tab_xpath
        )

        assert leave.validate_element_visible(
            leave.my_leave_tab_xpath
        )

        assert leave.validate_element_visible(
            leave.entitlements_tab_xpath
        )

        assert leave.validate_element_visible(
            leave.reports_tab_xpath
        )

        assert leave.validate_element_visible(
            leave.configure_tab_xpath
        )

        assert leave.validate_element_visible(
            leave.leave_list_tab_xpath
        )

        assert leave.validate_element_visible(
            leave.assign_leave_tab_xpath
        )

    def test_entitlements_dropdown_validation(self, login_setup):

        self.driver = login_setup

        leave = LeavePage(self.driver)

        leave.click_element(leave.leave_menu_xpath)

        leave.click_element(leave.entitlements_tab_xpath)

        assert leave.validate_element_visible(
            leave.add_entitlements_xpath
        )

        assert leave.validate_element_visible(
            leave.employee_entitlements_xpath
        )

        assert leave.validate_element_visible(
            leave.my_entitlements_xpath
        )

    def test_reports_dropdown_validation(self, login_setup):

        self.driver = login_setup

        leave = LeavePage(self.driver)

        leave.click_element(leave.leave_menu_xpath)

        leave.click_element(leave.reports_tab_xpath)

        assert leave.validate_element_visible(
            leave.leave_entitlements_report_xpath
        )

        assert leave.validate_element_visible(
            leave.my_leave_entitlements_report_xpath
        )

    def test_configure_dropdown_validation(self, login_setup):

        self.driver = login_setup

        leave = LeavePage(self.driver)

        leave.click_element(leave.leave_menu_xpath)

        leave.click_element(leave.configure_tab_xpath)

        assert leave.validate_element_visible(
            leave.leave_period_xpath
        )

        assert leave.validate_element_visible(
            leave.leave_types_xpath
        )

        assert leave.validate_element_visible(
            leave.work_week_xpath
        )

        assert leave.validate_element_visible(
            leave.holidays_xpath
        )

    def test_apply_leave_page_validation(self, login_setup):

        self.driver = login_setup

        leave = LeavePage(self.driver)

        leave.click_element(leave.leave_menu_xpath)

        leave.click_element(leave.apply_tab_xpath)

        assert leave.validate_element_visible(
            leave.apply_leave_header_xpath
        )

    def test_my_leave_page_validation(self, login_setup):

        self.driver = login_setup

        leave = LeavePage(self.driver)

        leave.click_element(leave.leave_menu_xpath)

        leave.click_element(leave.my_leave_tab_xpath)

        assert leave.validate_element_visible(
            leave.my_leave_header_xpath
        )

    def test_leave_list_page_validation(self, login_setup):

        self.driver = login_setup

        leave = LeavePage(self.driver)

        leave.click_element(leave.leave_menu_xpath)

        leave.click_element(leave.leave_list_tab_xpath)

        assert leave.validate_element_visible(
            leave.leave_list_header_xpath
        )

    def test_assign_leave_page_validation(self, login_setup):

        self.driver = login_setup

        leave = LeavePage(self.driver)

        leave.click_element(leave.leave_menu_xpath)

        leave.click_element(leave.assign_leave_tab_xpath)

        assert leave.validate_element_visible(
            leave.assign_leave_header_xpath
        )