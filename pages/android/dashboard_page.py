import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    CONTROLS_TAB = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Controls")'
    )

    SETTINGS_TAB = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Settings")'
    )

    NAVIGATE_UP = (
        AppiumBy.ACCESSIBILITY_ID,
        "Navigate up"
    )

    def __init__(self, driver):
        self.driver = driver

    def verify_dashboard_loaded(self):

        try:
            time.sleep(3)

            current_package = self.driver.current_package
            current_activity = self.driver.current_activity

            print("========== App State ==========")
            print("Current Package :", current_package)
            print("Current Activity:", current_activity)
            print("===============================")

            if current_package == "com.openvehicles.OVMS":
                print("Dashboard loaded successfully")
                return True

            print("OVMS app is not active")
            return False

        except Exception as e:
            print("Dashboard verification failed")
            print(e)
            return False

    def open_controls(self):

        try:
            controls = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CONTROLS_TAB)
            )

            controls.click()
            print("Controls opened")

            time.sleep(2)

            return True

        except Exception as e:
            print("Failed to open Controls")
            print(e)
            return False

    def open_settings(self):

        try:
            settings = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.SETTINGS_TAB)
            )

            settings.click()
            print("Settings opened")

            time.sleep(2)

            return True

        except Exception as e:
            print("Failed to open Settings")
            print(e)
            return False

    def navigate_up(self):

        try:
            navigate_up = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.NAVIGATE_UP)
            )

            navigate_up.click()
            print("Navigate Up clicked")

            time.sleep(2)

            return True

        except Exception as e:
            print("Failed to navigate up")
            print(e)
            return False
