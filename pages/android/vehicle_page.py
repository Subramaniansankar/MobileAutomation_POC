from appium.webdriver.common.appiumby import AppiumBy
import time


class VehiclePage:

    def __init__(self, driver):
        self.driver = driver


    def scroll_to_vehicle_information(self):

        print("========== Inside Scroll Method ==========")

        try:

            # First scroll
            self.driver.execute_script(
                "mobile: scrollGesture",
                {
                    "left": 100,
                    "top": 300,
                    "width": 800,
                    "height": 1200,
                    "direction": "down",
                    "percent": 0.8
                }
            )

            time.sleep(2)

            print("✅ First Scroll Executed")


            # Second scroll
            self.driver.execute_script(
                "mobile: scrollGesture",
                {
                    "left": 100,
                    "top": 300,
                    "width": 800,
                    "height": 1200,
                    "direction": "down",
                    "percent": 0.8
                }
            )

            time.sleep(2)

            print("✅ Second Scroll Executed")


            return True


        except Exception as e:

            print("❌ Scroll Failed")
            print(e)

            return False



    def get_vehicle_information(self):

        time.sleep(2)

        elements = self.driver.find_elements(
            AppiumBy.CLASS_NAME,
            "android.widget.TextView"
        )


        print(f"Total TextView elements: {len(elements)}")


        print("\n========== Vehicle Information ==========\n")


        vehicle_data = []


        for element in elements:

            try:

                text = element.text.strip()

                if text:

                    vehicle_data.append(text)

                    print(text)


            except Exception:

                pass


        print("\n=========================================\n")


        return vehicle_data