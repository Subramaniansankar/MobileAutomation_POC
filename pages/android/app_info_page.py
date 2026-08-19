from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ApplicationInfoPage:

    def __init__(self, driver):
        self.driver = driver

    # =========================================================
    # Scroll to Application Information
    # =========================================================

    def scroll_to_application_information(self):

        try:

            print(
                "========== Scrolling to Application Information =========="
            )

            # First scroll
            self.driver.execute_script(
                "mobile: scrollGesture",
                {
                    "left": 100,
                    "top": 500,
                    "width": 800,
                    "height": 1200,
                    "direction": "down",
                    "percent": 0.8
                }
            )

            print("✅ First Scroll Executed")

            time.sleep(1)

            # Second scroll
            self.driver.execute_script(
                "mobile: scrollGesture",
                {
                    "left": 100,
                    "top": 500,
                    "width": 800,
                    "height": 1200,
                    "direction": "down",
                    "percent": 0.8
                }
            )

            print("✅ Second Scroll Executed")

            time.sleep(2)

            return True

        except Exception as e:

            print(
                "❌ Failed to scroll to Application Information"
            )

            print(
                "Error:",
                e
            )

            return False

    # =========================================================
    # Get Application Information
    # =========================================================

    def get_application_information(self):

        try:

            text_elements = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.presence_of_all_elements_located(
                    (
                        AppiumBy.CLASS_NAME,
                        "android.widget.TextView"
                    )
                )
            )

            application_data = []

            print("")
            print(
                "========== Application Information =========="
            )
            print("")

            for element in text_elements:

                text = element.text.strip()

                if text:

                    print(
                        "FOUND:",
                        text
                    )

                    if (
                        "App:" in text
                        or "OVMS Version" in text
                        or "OVMS Server Version" in text
                        or "Server:" in text
                    ):

                        application_data.append(
                            text
                        )

            print("")
            print(
                "Filtered Application Data:"
            )

            for item in application_data:
                print(item)

            print("")
            print(
                "============================================="
            )

            return application_data

        except Exception as e:

            print(
                "❌ Failed to retrieve Application Information"
            )

            print(
                "Error:",
                e
            )

            return []