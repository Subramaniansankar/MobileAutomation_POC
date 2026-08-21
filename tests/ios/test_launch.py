import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    # =========================================================
    # iOS LOCATORS
    # =========================================================

    # Dynamic battery percentage shown on Status screen
    BATTERY_PERCENTAGE = (
        AppiumBy.IOS_PREDICATE,
        "name MATCHES '^[0-9]{1,3}%$'"
    )

    # Status menu
    STATUS_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Status"
    )

    # Settings menu
    SETTINGS_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Settings"
    )

    # =========================================================
    # VERIFY STATUS SCREEN
    # =========================================================

    def verify_dashboard_loaded(self):

        print("")
        print("========== VERIFYING iOS STATUS SCREEN ==========")

        # First try battery percentage
        try:

            battery = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    self.BATTERY_PERCENTAGE
                )
            )

            print(
                f"Battery Percentage : {battery.text}"
            )

            print("✅ iOS Status screen loaded successfully")
            print("=================================================")

            return True

        except TimeoutException:

            print(
                "Battery percentage not found - checking Status menu..."
            )

        # Fallback: verify Status button
        try:

            status = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.presence_of_element_located(
                    self.STATUS_BUTTON
                )
            )

            if status.is_displayed():

                print("✅ Status menu found")
                print("✅ iOS Status screen loaded successfully")
                print("=================================================")

                return True

        except TimeoutException:

            print("❌ Status menu not found")

        print("❌ iOS Status screen verification failed")
        print("=================================================")

        return False

    # =========================================================
    # OPEN SETTINGS
    # =========================================================

    def open_settings(self):

        try:

            print("Waiting for Settings...")

            settings_button = WebDriverWait(
                self.driver,
                15
            ).until(
                EC.presence_of_element_located(
                    self.SETTINGS_BUTTON
                )
            )

            print("✅ Settings found")

            settings_button.click()

            print("✅ Settings clicked")

            time.sleep(2)

            return True

        except TimeoutException:

            print("❌ Settings button not found")

            return False

        except Exception as e:

            print("❌ Failed to open Settings")
            print("Error:", e)

            return False