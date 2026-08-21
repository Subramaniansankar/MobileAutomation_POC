import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    # =========================================================
    # LOCATORS
    # =========================================================

    BATTERY_PERCENTAGE = (
        AppiumBy.IOS_PREDICATE,
        "name MATCHES '^[0-9]{1,3}%$'"
    )

    STATUS_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Status"
    )

    SETTINGS_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Settings"
    )

    # =========================================================
    # VERIFY STATUS SCREEN
    # =========================================================

    def verify_dashboard_loaded(self):

        print("")
        print("========== VERIFYING iOS STATUS ==========")

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

            print(
                "✅ Status screen loaded successfully"
            )

            print(
                "=========================================="
            )

            return True

        except TimeoutException:

            print(
                "Battery percentage not found - checking Status..."
            )

        try:

            status_elements = self.driver.find_elements(
                AppiumBy.ACCESSIBILITY_ID,
                "Status"
            )

            for element in status_elements:

                if element.is_displayed():

                    print(
                        "✅ Status element found"
                    )

                    print(
                        "✅ Status screen loaded successfully"
                    )

                    print(
                        "=========================================="
                    )

                    return True

        except Exception as e:

            print(
                "Error while verifying Status:",
                e
            )

        print(
            "❌ Status screen verification failed"
        )

        print(
            "=========================================="
        )

        return False

    # =========================================================
    # NAVIGATE TO STATUS
    # =========================================================

    def navigate_to_status(self):

        try:

            print(
                "Checking whether Status screen is already open..."
            )

            # -------------------------------------------------
            # Already on Status?
            # -------------------------------------------------

            try:

                battery = WebDriverWait(
                    self.driver,
                    5
                ).until(
                    EC.visibility_of_element_located(
                        self.BATTERY_PERCENTAGE
                    )
                )

                print(
                    f"✅ Already on Status screen - Battery: {battery.text}"
                )

                return True

            except TimeoutException:

                print(
                    "Not currently on Status screen"
                )

            # -------------------------------------------------
            # Find Status button
            # -------------------------------------------------

            print(
                "Searching for Status button..."
            )

            status_elements = self.driver.find_elements(
                AppiumBy.ACCESSIBILITY_ID,
                "Status"
            )

            print(
                "Status elements found:",
                len(status_elements)
            )

            for element in status_elements:

                try:

                    if element.is_displayed():

                        element.click()

                        print(
                            "✅ Status clicked"
                        )

                        time.sleep(3)

                        return True

                except Exception:

                    continue

            # -------------------------------------------------
            # Predicate fallback
            # -------------------------------------------------

            print(
                "Trying Status using iOS predicate..."
            )

            status_button = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.IOS_PREDICATE,
                        'name == "Status"'
                    )
                )
            )

            status_button.click()

            print(
                "✅ Status clicked using predicate"
            )

            time.sleep(3)

            return True

        except TimeoutException:

            print(
                "❌ Status button not found"
            )

            return False

        except Exception as e:

            print(
                "❌ Failed to navigate to Status"
            )

            print(
                "Error:",
                e
            )

            return False

    # =========================================================
    # OPEN SETTINGS
    # =========================================================

    def open_settings(self):

        try:

            print(
                "Searching for Settings..."
            )

            settings_elements = self.driver.find_elements(
                AppiumBy.ACCESSIBILITY_ID,
                "Settings"
            )

            print(
                "Settings elements found:",
                len(settings_elements)
            )

            for element in settings_elements:

                try:

                    if element.is_displayed():

                        element.click()

                        print(
                            "✅ Settings clicked"
                        )

                        time.sleep(2)

                        return True

                except Exception:

                    continue

            print(
                "Trying Settings using iOS predicate..."
            )

            settings_button = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.IOS_PREDICATE,
                        'name == "Settings"'
                    )
                )
            )

            settings_button.click()

            print(
                "✅ Settings clicked using predicate"
            )

            time.sleep(2)

            return True

        except TimeoutException:

            print(
                "❌ Settings button not found"
            )

            return False

        except Exception as e:

            print(
                "❌ Failed to open Settings"
            )

            print(
                "Error:",
                e
            )

            return False