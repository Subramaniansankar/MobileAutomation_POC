from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class SettingsPage:

    # =========================================================
    # LOCATORS
    # =========================================================

    NEW_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "New"
    )

    VEHICLE_ID = (
        AppiumBy.IOS_PREDICATE,
        'value == "Vehicle ID"'
    )

    VEHICLE_LABEL = (
        AppiumBy.IOS_PREDICATE,
        'value == "Vehicle Label"'
    )

    SERVER_PASSWORD = (
        AppiumBy.IOS_PREDICATE,
        'value == "OVMS Server Password"'
    )

    MODULE_PASSWORD = (
        AppiumBy.IOS_PREDICATE,
        'value == "OVMS Module Password"'
    )

    CARS_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Cars"
    )

    STATUS_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Status"
    )

    # =========================================================
    # CONSTRUCTOR
    # =========================================================

    def __init__(self, driver):
        self.driver = driver

    # =========================================================
    # OPEN NEW VEHICLE
    # =========================================================

    def open_new_vehicle(self):

        try:

            print("Waiting for New button...")

            new_button = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(
                    self.NEW_BUTTON
                )
            )

            new_button.click()

            print("✅ New button clicked")
            print("New Vehicle screen opened")

            time.sleep(2)

            return True

        except TimeoutException:

            print("❌ New button not found")
            return False

        except Exception as e:

            print("❌ Failed to open New Vehicle")
            print("Error:", e)

            return False

    # =========================================================
    # ENTER VEHICLE ID
    # =========================================================

    def enter_vehicle_id(self, vehicle_id):

        try:

            vehicle_id_field = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    self.VEHICLE_ID
                )
            )

            vehicle_id_field.clear()
            vehicle_id_field.send_keys(vehicle_id)

            print(
                f"✅ Vehicle ID entered: {vehicle_id}"
            )

            return True

        except Exception as e:

            print("❌ Failed to enter Vehicle ID")
            print("Error:", e)

            return False

    # =========================================================
    # ENTER VEHICLE LABEL
    # =========================================================

    def enter_vehicle_label(self, vehicle_label):

        try:

            vehicle_label_field = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    self.VEHICLE_LABEL
                )
            )

            vehicle_label_field.clear()
            vehicle_label_field.send_keys(
                vehicle_label
            )

            print(
                f"✅ Vehicle Label entered: {vehicle_label}"
            )

            return True

        except Exception as e:

            print("❌ Failed to enter Vehicle Label")
            print("Error:", e)

            return False

    # =========================================================
    # ENTER SERVER PASSWORD
    # =========================================================

    def enter_server_password(
        self,
        server_password
    ):

        try:

            server_password_field = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    self.SERVER_PASSWORD
                )
            )

            server_password_field.clear()

            server_password_field.send_keys(
                server_password
            )

            print(
                "✅ OVMS Server Password entered"
            )

            return True

        except Exception as e:

            print(
                "❌ Failed to enter OVMS Server Password"
            )

            print("Error:", e)

            return False

    # =========================================================
    # ENTER MODULE PASSWORD
    # =========================================================

    def enter_module_password(
        self,
        module_password
    ):

        try:

            module_password_field = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    self.MODULE_PASSWORD
                )
            )

            module_password_field.clear()

            module_password_field.send_keys(
                module_password
            )

            print(
                "✅ OVMS Module Password entered"
            )

            return True

        except Exception as e:

            print(
                "❌ Failed to enter OVMS Module Password"
            )

            print("Error:", e)

            return False

    # =========================================================
    # ENTER ALL VEHICLE DETAILS
    # =========================================================

    def enter_vehicle_details(
        self,
        vehicle_id,
        vehicle_label,
        server_password,
        module_password
    ):

        if not self.enter_vehicle_id(
            vehicle_id
        ):
            return False

        if not self.enter_vehicle_label(
            vehicle_label
        ):
            return False

        if not self.enter_server_password(
            server_password
        ):
            return False

        if not self.enter_module_password(
            module_password
        ):
            return False

        return True

    # =========================================================
    # NAVIGATE BACK TO CARS
    # =========================================================

    def navigate_to_cars(self):

        try:

            print("Waiting for Cars button...")

            cars_button = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(
                    self.CARS_BUTTON
                )
            )

            cars_button.click()

            print("✅ Cars button clicked")
            print("Returned to Cars screen")

            time.sleep(2)

            return True

        except TimeoutException:

            print("❌ Cars button not found")
            return False

        except Exception as e:

            print("❌ Failed to navigate to Cars")
            print("Error:", e)

            return False

    # =========================================================
    # NAVIGATE TO STATUS
    # =========================================================

    def navigate_to_status(self):

        try:

            print("Waiting for Status button...")

            status_button = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(
                    self.STATUS_BUTTON
                )
            )

            status_button.click()

            print("✅ Status button clicked")
            print("Returned to Status screen")

            time.sleep(2)

            return True

        except TimeoutException:

            print("❌ Status button not found")
            return False

        except Exception as e:

            print("❌ Failed to navigate to Status")
            print("Error:", e)

            return False

    # =========================================================
    # ADD NEW VEHICLE FLOW
    # =========================================================

    def add_new_vehicle(
        self,
        vehicle_id,
        vehicle_label,
        server_password,
        module_password
    ):

        try:

            print("")
            print("==============================================")
            print("STARTING iOS ADD NEW VEHICLE FLOW")
            print("==============================================")

            # STEP 1 - Click New
            if not self.open_new_vehicle():
                return False

            # STEP 2 - Enter Vehicle Details
            if not self.enter_vehicle_details(
                vehicle_id=vehicle_id,
                vehicle_label=vehicle_label,
                server_password=server_password,
                module_password=module_password
            ):
                return False

            print("")
            print("==============================================")
            print(
                "✅ NEW VEHICLE DETAILS ENTERED SUCCESSFULLY"
            )
            print("==============================================")

            return True

        except Exception as e:

            print("❌ Failed to add new vehicle")
            print("Error:", e)

            return False