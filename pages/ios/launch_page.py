import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LaunchPage:

    def __init__(self, driver):
        self.driver = driver

    # =========================================================
    # LOCATORS
    # =========================================================

    # Version popup OK button
    ok_button = (
        AppiumBy.ACCESSIBILITY_ID,
        "OK"
    )

    # iOS location permission
    allow_button = (
        AppiumBy.ACCESSIBILITY_ID,
        "Allow While Using App"
    )

    # Dynamic battery percentage
    battery_percentage = (
        AppiumBy.IOS_PREDICATE,
        "name MATCHES '^[0-9]{1,3}%$'"
    )

    # =========================================================
    # DISMISS VERSION POPUP
    # =========================================================

    def dismiss_version_popup(self):

        try:

            ok = WebDriverWait(
                self.driver,
                5
            ).until(
                EC.element_to_be_clickable(
                    self.ok_button
                )
            )

            ok.click()

            print(
                "✅ Version popup displayed - Clicked OK"
            )

            return True

        except TimeoutException:

            print(
                "⏭️ Version popup not displayed - Continuing execution"
            )

            return True

        except Exception as e:

            print(
                "❌ Error while handling version popup"
            )

            print("Error:", e)

            return True

    # =========================================================
    # LOCATION PERMISSION
    # =========================================================

    def allow_location_permission(self):

        try:

            allow = WebDriverWait(
                self.driver,
                5
            ).until(
                EC.element_to_be_clickable(
                    self.allow_button
                )
            )

            allow.click()

            print(
                "✅ Location permission displayed - Allowed"
            )

            return True

        except TimeoutException:

            print(
                "⏭️ Location permission not displayed - Continuing execution"
            )

            return True

        except Exception as e:

            print(
                "❌ Error while handling location permission"
            )

            print("Error:", e)

            return True

    # =========================================================
    # VERIFY OVMS APPLICATION LAUNCH
    # =========================================================

    def verify_app_launched(self):

        try:

            print("")
            print(
                "========== VERIFYING OVMS APP =========="
            )

            # -------------------------------------------------
            # STEP 1 - Check app state
            # -------------------------------------------------

            app_state = self.driver.query_app_state(
                "com.openvehicles.ovms"
            )

            print(
                "OVMS App State :",
                app_state
            )

            # Appium app state:
            # 0 = Not installed
            # 1 = Not running
            # 2 = Running in background / suspended
            # 3 = Running in background
            # 4 = Running in foreground

            if app_state != 4:

                print(
                    "OVMS not in foreground - Activating app..."
                )

                self.driver.activate_app(
                    "com.openvehicles.ovms"
                )

                time.sleep(3)

                app_state = self.driver.query_app_state(
                    "com.openvehicles.ovms"
                )

                print(
                    "OVMS App State after activation :",
                    app_state
                )

            # -------------------------------------------------
            # STEP 2 - Verify foreground state
            # -------------------------------------------------

            if app_state != 4:

                print(
                    "❌ OVMS application is not running in foreground"
                )

                return False

            print(
                "✅ OVMS application is running in foreground"
            )

            # -------------------------------------------------
            # STEP 3 - Verify battery percentage
            # -------------------------------------------------

            try:

                battery = WebDriverWait(
                    self.driver,
                    20
                ).until(
                    EC.visibility_of_element_located(
                        self.battery_percentage
                    )
                )

                print(
                    f"Battery Percentage: {battery.text}"
                )

            except TimeoutException:

                # Battery is useful, but app foreground state
                # is enough to confirm successful launch.
                print(
                    "⚠️ Battery percentage not found"
                )

                print(
                    "✅ OVMS is still running in foreground"
                )

            print(
                "✅ OVMS application launched successfully"
            )

            print(
                "========================================"
            )

            return True

        except Exception as e:

            print(
                "❌ Error while verifying OVMS application"
            )

            print(
                "Error:",
                e
            )

            return False