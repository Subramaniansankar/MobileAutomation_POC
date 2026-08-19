import time

from pages.android.launch_page import LaunchPage
from pages.android.dashboard_page import DashboardPage
from pages.android.vehicle_page import VehiclePage
from pages.android.charging_page import ChargingPage
from pages.android.settings_page import SettingsPage


class TestVehicle:

    def test_vehicle_end_to_end_flow(self, driver):

        # =====================================================
        # STEP 1: LAUNCH OVMS
        # =====================================================

        driver.activate_app(
            "com.openvehicles.OVMS"
        )

        time.sleep(3)

        launch = LaunchPage(driver)

        launch.dismiss_version_popup()
        launch.allow_location_permission()

        assert launch.verify_app_launched(), \
            "OVMS application did not launch successfully"

        print(
            "========== STEP 1: OVMS LAUNCHED =========="
        )

        # =====================================================
        # STEP 2: START / STOP CHARGING
        # =====================================================

        charging = ChargingPage(driver)

        charging.start_stop_charging(
            confirm=True
        )

        print(
            "========== STEP 2: CHARGING START/STOP COMPLETED =========="
        )

        # =====================================================
        # STEP 3: VERIFY DASHBOARD
        # =====================================================

        dashboard = DashboardPage(driver)

        assert dashboard.verify_dashboard_loaded(), \
            "Dashboard is not loaded"

        print(
            "========== STEP 3: DASHBOARD VERIFIED =========="
        )

        # =====================================================
        # STEP 4: OPEN CONTROLS
        # =====================================================

        assert dashboard.open_controls(), \
            "Failed to open Controls menu"

        print(
            "========== STEP 4: CONTROLS OPENED =========="
        )

        # =====================================================
        # STEP 5: BACK TO DASHBOARD
        # =====================================================

        assert dashboard.navigate_up(), \
            "Failed to navigate back from Controls"

        time.sleep(2)

        assert dashboard.verify_dashboard_loaded(), \
            "Dashboard is not loaded after navigating back"

        print(
            "========== STEP 5: BACK TO DASHBOARD =========="
        )

        # =====================================================
        # STEP 6: VERIFY VEHICLE INFORMATION
        # =====================================================

        vehicle = VehiclePage(driver)

        assert vehicle.scroll_to_vehicle_information(), \
            "Failed to scroll to Vehicle Information"

        vehicle_data = vehicle.get_vehicle_information()

        assert vehicle_data, \
            "Vehicle information was not displayed"

        print(
            "========== STEP 6: VEHICLE INFORMATION VERIFIED =========="
        )

        # =====================================================
        # STEP 7: OPEN SETTINGS
        # =====================================================

        assert dashboard.open_settings(), \
            "Failed to open Settings"

        print(
            "========== STEP 7: SETTINGS OPENED =========="
        )

        settings = SettingsPage(driver)

        # =====================================================
        # TEST DATA
        # =====================================================

        vehicle_id = "TEST_VEHICLE_002"

        vehicle_label = "Automation Vehicle"

        server_password = "TEST_SERVER_PASSWORD"

        module_password = "TEST_MODULE_PASSWORD"

        # =====================================================
        # STEP 8: CLICK + AND ADD NEW VEHICLE
        # =====================================================

        assert settings.add_new_vehicle(
            vehicle_id=vehicle_id,
            vehicle_label=vehicle_label,
            server_password=server_password,
            module_password=module_password
        ), "Failed to add new vehicle"

        print(
            "========== STEP 8: NEW VEHICLE ADDED =========="
        )

        time.sleep(2)

        # =====================================================
        # STEP 9: PRINT CURRENT SCREEN
        # =====================================================

        print("==============================================")
        print("APP STATE AFTER ADDING VEHICLE")
        print(
            "Current Package :",
            driver.current_package
        )
        print(
            "Current Activity:",
            driver.current_activity
        )
        print("==============================================")

        # =====================================================
        # STEP 10: NAVIGATE BACK
        # =====================================================

        assert settings.navigate_up(), \
            "Failed to navigate back after adding vehicle"

        time.sleep(2)

        print(
            "========== STEP 10: NAVIGATED BACK =========="
        )

        # =====================================================
        # FINAL STATE
        # =====================================================

        print("==============================================")
        print("TC_003 COMPLETED")
        print("New Vehicle ID    :", vehicle_id)
        print("New Vehicle Label :", vehicle_label)
        print("Current Package   :", driver.current_package)
        print("Current Activity  :", driver.current_activity)
        print("==============================================")