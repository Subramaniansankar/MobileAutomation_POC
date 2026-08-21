import time

from pages.ios.launch_page import LaunchPage
from pages.ios.dashboard_page import DashboardPage
from pages.ios.settings_page import SettingsPage


class TestVehicle:

    def test_add_new_vehicle(self, driver):

        # =====================================================
        # STEP 1: Clean Launch OVMS
        # =====================================================

        driver.terminate_app(
            "com.openvehicles.ovms"
        )

        time.sleep(2)

        driver.activate_app(
            "com.openvehicles.ovms"
        )

        time.sleep(4)

        launch = LaunchPage(driver)

        launch.dismiss_version_popup()
        launch.allow_location_permission()

        assert launch.verify_app_launched(), \
            "OVMS application did not launch successfully"

        print(
            "========== STEP 1: OVMS LAUNCHED =========="
        )

        # =====================================================
        # STEP 2: Navigate to Status
        # =====================================================

        dashboard = DashboardPage(driver)

        assert dashboard.navigate_to_status(), \
            "Failed to navigate to Status"

        time.sleep(2)

        assert dashboard.verify_dashboard_loaded(), \
            "Status screen is not loaded"

        print(
            "========== STEP 2: STATUS VERIFIED =========="
        )

        # =====================================================
        # STEP 3: Open Settings
        # =====================================================

        assert dashboard.open_settings(), \
            "Failed to open Settings"

        print(
            "========== STEP 3: SETTINGS OPENED =========="
        )

        time.sleep(2)

        # =====================================================
        # STEP 4: Add New Vehicle
        # =====================================================

        settings = SettingsPage(driver)

        vehicle_id = "IOS_TEST_VEHICLE_001"
        vehicle_label = "iOS Automation Vehicle"
        server_password = "TEST_SERVER_PASSWORD"
        module_password = "TEST_MODULE_PASSWORD"

        assert settings.add_new_vehicle(
            vehicle_id=vehicle_id,
            vehicle_label=vehicle_label,
            server_password=server_password,
            module_password=module_password
        ), "Failed to add new vehicle in iOS"

        print(
            "========== STEP 4: VEHICLE DETAILS ENTERED =========="
        )

        # =====================================================
        # STEP 5: Navigate Back to Cars
        # =====================================================

        assert settings.navigate_to_cars(), \
            "Failed to navigate back to Cars"

        print(
            "========== STEP 5: RETURNED TO CARS =========="
        )

        time.sleep(2)

        # =====================================================
        # STEP 6: Navigate to Status
        # =====================================================

        assert settings.navigate_to_status(), \
            "Failed to navigate to Status"

        print(
            "========== STEP 6: STATUS OPENED =========="
        )

        time.sleep(2)

        # =====================================================
        # STEP 7: Verify Status
        # =====================================================

        assert dashboard.verify_dashboard_loaded(), \
            "Status screen is not loaded after adding vehicle"

        print(
            "========== STEP 7: STATUS VERIFIED =========="
        )

        # =====================================================
        # FINAL RESULT
        # =====================================================

        print("")
        print("==============================================")
        print("TC - iOS ADD NEW VEHICLE COMPLETED")
        print("Vehicle ID    :", vehicle_id)
        print("Vehicle Label :", vehicle_label)
        print("Final Screen  : Status")
        print("==============================================")