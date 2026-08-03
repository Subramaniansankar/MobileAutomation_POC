from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LaunchPage:

    def __init__(self, driver):
        self.driver = driver


    ok_button = (
        AppiumBy.ACCESSIBILITY_ID,
        "OK"
    )


    allow_button = (
        AppiumBy.ACCESSIBILITY_ID,
        "Allow"
    )


    battery_percentage = (
        AppiumBy.IOS_PREDICATE,
        "name MATCHES '\\\\d+%'"
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
        try:
            battery = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.battery_percentage)
            )

            print(f"Battery Percentage: {battery.text}")
            return True

        except TimeoutException:

            print("Current Page Source")
            print(self.driver.page_source)

            return False

        except TimeoutException:
            print("❌ Battery percentage not displayed")
            return False