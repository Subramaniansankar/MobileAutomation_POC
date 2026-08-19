from pages.ios.launch_page import LaunchPage
from pages.ios.dashboard_page import DashboardPage


class TestDashboard:

    def test_verify_dashboard(self, driver):

        launch = LaunchPage(driver)

        launch.dismiss_version_popup()
        launch.allow_location_permission()

        dashboard = DashboardPage(driver)

        assert dashboard.verify_dashboard_loaded()