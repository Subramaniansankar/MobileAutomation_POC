from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LaunchPage:

    def __init__(self, driver):
        self.driver = driver


    # Version popup OK button
    ok_button = (
        AppiumBy.ACCESSIBILITY_ID,
        "OK"
    )


    # Location permission button
    allow_button = (
        AppiumBy.ID,
        "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    )


    # Battery percentage text
    battery_percentage = (
        AppiumBy.XPATH,
        "//android.widget.TextView[contains(@text,'%')]"
    )


    def dismiss_version_popup(self):
        try:
            ok = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.ok_button)
            )

            ok.click()
            print("✅ Version popup displayed - Clicked OK")

        except TimeoutException:
            print("⏭️ Version popup not displayed - Continuing execution")


    def allow_location_permission(self):
        try:
            allow = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.allow_button)
            )

            allow.click()
            print("✅ Location permission displayed - Clicked Allow")

        except TimeoutException:
            print("⏭️ Location permission not displayed - Continuing execution")


    def verify_app_launched(self):

        expected_package = "com.openvehicles.OVMS"

        actual_package = self.driver.current_package
        actual_activity = self.driver.current_activity

        print("========== App State ==========")
        print(f"Current Package : {actual_package}")
        print(f"Current Activity: {actual_activity}")
        print("===============================")

        if actual_package == expected_package:
            print("✅ OVMS application launched successfully")
            return True

        print("❌ OVMS application is not active")
        return False