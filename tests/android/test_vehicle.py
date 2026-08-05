import time

from pages.android.launch_page import LaunchPage
from pages.android.dashboard_page import DashboardPage
from pages.android.vehicle_page import VehiclePage
from pages.android.charging_page import ChargingPage
from pages.android.settings_page import SettingsPage


class TestVehicle:

    def test_verify_vehicle_information(self, driver):

        launch = LaunchPage(driver)

        launch.dismiss_version_popup()
        launch.allow_location_permission()

        driver.activate_app("com.openvehicles.OVMS")
        time.sleep(3)

        assert launch.verify_app_launched(), "OVMS application did not launch successfully"

        print("========== STEP 1: OVMS LAUNCHED ==========")

        charging = ChargingPage(driver)

        charging.start_stop_charging(confirm=True)

        print("========== STEP 2: CHARGING START/STOP COMPLETED ==========")

        dashboard = DashboardPage(driver)

        assert dashboard.verify_dashboard_loaded(), "Dashboard is not loaded"

        print("========== STEP 3: DASHBOARD VERIFIED ==========")

        assert dashboard.open_controls(), "Failed to open Controls menu"

        print("========== STEP 4: CONTROLS OPENED ==========")

        assert dashboard.navigate_up(), "Failed to navigate back from Controls"

        time.sleep(2)

        assert dashboard.verify_dashboard_loaded(), \
            "Dashboard is not loaded after navigating back"

        print("========== STEP 5: BACK TO DASHBOARD ==========")

        vehicle = VehiclePage(driver)

        assert vehicle.scroll_to_vehicle_information(), \
            "Failed to scroll to Vehicle Information"

        print("========== STEP 6: VEHICLE DETAILS ==========")

        vehicle_data = vehicle.get_vehicle_information()

        assert vehicle_data, "Vehicle information was not displayed"

        assert dashboard.open_settings(), "Failed to open Settings"

        print("========== STEP 7: SETTINGS OPENED ==========")

        settings = SettingsPage(driver)

        vehicle_id = "TEST_VEHICLE_ID"
        vehicle_label = "Test Vehicle"
        server_password = "TEST_SERVER_PASSWORD"
        module_password = "TEST_MODULE_PASSWORD"

        assert settings.add_vehicle(
            vehicle_id=vehicle_id,
            vehicle_label=vehicle_label,
            server_password=server_password,
            module_password=module_password
        ), "Failed to add vehicle"

        print("========== STEP 8: VEHICLE ADDED AND SAVED ==========")

        time.sleep(2)

        assert dashboard.verify_dashboard_loaded(), \
            "Dashboard is not loaded after adding vehicle"

        print("========== STEP 9: FINAL DASHBOARD VERIFIED ==========")

        print("==============================================")
        print("Final App State")
        print("Current Package :", driver.current_package)
        print("Current Activity:", driver.current_activity)
        print("==============================================")
