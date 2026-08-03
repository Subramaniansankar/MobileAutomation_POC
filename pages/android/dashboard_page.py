from appium.webdriver.common.appiumby import AppiumBy
import time


class DashboardPage:

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


            print("❌ OVMS app is not active")

            return False


        except Exception as e:

            print("Dashboard verification failed")
            print(e)

            return False