import time

from pages.android.launch_page import LaunchPage
from pages.android.dashboard_page import DashboardPage
from pages.android.app_info_page import ApplicationInfoPage


class TestApplicationInformation:

    def test_verify_application_information(self, driver):

        # =====================================================
        # STEP 1: Launch OVMS
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
        # STEP 2: Verify Dashboard
        # =====================================================

        dashboard = DashboardPage(driver)

        assert dashboard.verify_dashboard_loaded(), \
            "Dashboard is not loaded"

        print(
            "========== STEP 2: DASHBOARD VERIFIED =========="
        )

        # =====================================================
        # STEP 3: Scroll to Application Information
        # =====================================================

        application_info = ApplicationInfoPage(
            driver
        )

        assert application_info.scroll_to_application_information(), \
            "Failed to scroll to Application Information"

        print(
            "========== STEP 3: APPLICATION INFORMATION LOCATED =========="
        )

        # =====================================================
        # STEP 4: Get Application Information
        # =====================================================

        app_data = application_info.get_application_information()

        assert app_data, \
            "Application Information was not displayed"

        print(
            "========== STEP 4: APPLICATION INFORMATION RETRIEVED =========="
        )

        # =====================================================
        # STEP 5: Verify Required Fields
        # =====================================================

        app_version_present = any(
            "App:" in item
            for item in app_data
        )

        ovms_version_present = any(
            "OVMS Version" in item
            for item in app_data
        )

        ovms_server_version_present = any(
            "OVMS Server Version" in item
            for item in app_data
        )

        server_present = any(
            "Server:" in item
            for item in app_data
        )

        assert app_version_present, \
            "App Version information is missing"

        assert ovms_version_present, \
            "OVMS Version information is missing"

        assert ovms_server_version_present, \
            "OVMS Server Version information is missing"

        assert server_present, \
            "Server information is missing"

        print(
            "========== STEP 5: REQUIRED FIELDS VERIFIED =========="
        )

        # =====================================================
        # FINAL RESULT
        # =====================================================

        print("")
        print(
            "=============================================="
        )

        print(
            "TC_004 APPLICATION INFORMATION VERIFIED"
        )

        print(
            "=============================================="
        )

        for item in app_data:
            print(item)

        print(
            "=============================================="
        )