import time

from pages.launch_page import LaunchPage
from pages.dashboard_page import DashboardPage
from pages.vehicle_page import VehiclePage
from pages.charging_page import ChargingPage


class TestVehicle:

    def test_verify_vehicle_information(self, driver):

        # Launch App
        launch = LaunchPage(driver)

        launch.dismiss_version_popup()
        launch.allow_location_permission()

        # Bring app to foreground
        driver.activate_app("com.openvehicles.OVMS")
        time.sleep(3)

        # Verify Dashboard
        dashboard = DashboardPage(driver)
        assert dashboard.verify_dashboard_loaded()

        # Scroll to Charging section
        vehicle = VehiclePage(driver)
        assert vehicle.scroll_to_vehicle_information()

        # Start / Stop Charging
        charging = ChargingPage(driver)
        charging.start_stop_charging(confirm=True)

        # Scroll further to Vehicle Information
        assert vehicle.scroll_to_vehicle_information()

        # Get Vehicle Information
        assert vehicle.get_vehicle_information()

        # Print current app details
        print("Current Package :", driver.current_package)
        print("Current Activity:", driver.current_activity)