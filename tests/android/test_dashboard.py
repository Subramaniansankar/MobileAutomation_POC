from pages.android.launch_page import LaunchPage
from pages.android.dashboard_page import DashboardPage


class TestDashboard:

    def test_verify_dashboard(self, driver):

        driver.activate_app("com.openvehicles.OVMS")

        launch = LaunchPage(driver)

        launch.dismiss_version_popup()
        launch.allow_location_permission()

        dashboard = DashboardPage(driver)

        assert dashboard.verify_dashboard_loaded()