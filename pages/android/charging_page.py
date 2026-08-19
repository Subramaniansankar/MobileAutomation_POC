from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ChargingPage:

    def __init__(self, driver):
        self.driver = driver

    CHARGING_BUTTON = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().resourceId("com.openvehicles.OVMS:id/action_button").instance(1)'
    )

    YES_BUTTON = (
        AppiumBy.ID,
        "android:id/button1"
    )

    NO_BUTTON = (
        AppiumBy.ID,
        "android:id/button2"
    )

    def start_stop_charging(self, confirm=True):

        charging = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.CHARGING_BUTTON)
        )

        charging.click()
        print("Charging button clicked")

        if confirm:

            yes = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.YES_BUTTON)
            )

            yes.click()
            print("YES button clicked")

        else:

            no = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.NO_BUTTON)
            )

            no.click()
            print("NO button clicked")