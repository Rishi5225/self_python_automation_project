from page_objects.dashboard_page import DashboardPage


class TestDashboard:

    def test_left_menu_validation(self, login_setup):

        self.driver = login_setup

        dashboard = DashboardPage(self.driver)

        assert dashboard.validate_admin_menu()
        assert dashboard.validate_pim_menu()
        assert dashboard.validate_leave_menu()
        assert dashboard.validate_time_menu()
        assert dashboard.validate_recruitment_menu()
        assert dashboard.validate_myinfo_menu()
        assert dashboard.validate_performance_menu()
        assert dashboard.validate_dashboard_menu()
        assert dashboard.validate_directory_menu()
        assert dashboard.validate_maintenance_menu()
        assert dashboard.validate_claim_menu()
        assert dashboard.validate_buzz_menu()