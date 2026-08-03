from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    BATTERY_PERCENTAGE = (
        AppiumBy.IOS_PREDICATE,
        "name MATCHES '^[0-9]{1,3}%$'"
    )

    def verify_dashboard_loaded(self):
        try:
            battery = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.BATTERY_PERCENTAGE)
            )

            print("\n========== Dashboard ==========")
            print(f"Battery Percentage : {battery.text}")
            print("Dashboard loaded successfully")
            print("================================\n")

            return True

        except TimeoutException:
            print("Dashboard verification failed")
            return False