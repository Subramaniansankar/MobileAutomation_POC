
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class SettingsPage:

    ADD_BUTTON = (
        AppiumBy.ID,
        "com.openvehicles.OVMS:id/mi_add"
    )

    EDIT_BUTTON = (
        AppiumBy.ID,
        "com.openvehicles.OVMS:id/btn_edit"
    )

    SAVE_BUTTON = (
        AppiumBy.ID,
        "com.openvehicles.OVMS:id/mi_save"
    )

    VEHICLE_ID = (
        AppiumBy.ID,
        "com.openvehicles.OVMS:id/txt_vehicle_id"
    )

    VEHICLE_LABEL = (
        AppiumBy.ID,
        "com.openvehicles.OVMS:id/txt_vehicle_label"
    )

    SERVER_PASSWORD = (
        AppiumBy.ID,
        "com.openvehicles.OVMS:id/txt_server_passwd"
    )

    MODULE_PASSWORD = (
        AppiumBy.ID,
        "com.openvehicles.OVMS:id/txt_module_passwd"
    )

    NAVIGATE_UP = (
        AppiumBy.ACCESSIBILITY_ID,
        "Navigate up"
    )

    NEVER_BUTTON = (
        AppiumBy.ID,
        "android:id/autofill_save_no"
    )

    def __init__(self, driver):
        self.driver = driver

    def open_existing_vehicle(self):

        try:

            print("Checking for existing vehicle...")

            edit_button = WebDriverWait(
                self.driver,
                5
            ).until(
                EC.element_to_be_clickable(
                    self.EDIT_BUTTON
                )
            )

            edit_button.click()

            print("Existing vehicle found")
            print("Edit button clicked")

            time.sleep(2)

            return True

        except TimeoutException:

            print("Existing vehicle not found")

            return False

        except Exception as e:

            print("Failed while checking existing vehicle")
            print("Error:", e)

            return False

    def open_add_vehicle(self):

        try:

            add_button = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(
                    self.ADD_BUTTON
                )
            )

            add_button.click()

            print("Add button clicked")

            time.sleep(2)

            return True

        except Exception as e:

            print("Failed to open Add Vehicle")
            print("Error:", e)

            return False

    def enter_vehicle_details(
        self,
        vehicle_id,
        vehicle_label,
        server_password,
        module_password
    ):

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

            print("Vehicle ID entered")

            vehicle_label_field = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    self.VEHICLE_LABEL
                )
            )

            vehicle_label_field.clear()
            vehicle_label_field.send_keys(vehicle_label)

            print("Vehicle Label entered")

            server_password_field = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    self.SERVER_PASSWORD
                )
            )

            server_password_field.clear()
            server_password_field.send_keys(server_password)

            print("Server password entered")

            module_password_field = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.visibility_of_element_located(
                    self.MODULE_PASSWORD
                )
            )

            module_password_field.clear()
            module_password_field.send_keys(module_password)

            print("Module/SMS password entered")

            return True

        except Exception as e:

            print("Failed to enter vehicle details")
            print("Error:", e)

            return False

    def click_save(self):

        try:

            print("Waiting for Save button...")

            save_button = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(
                    self.SAVE_BUTTON
                )
            )

            save_button.click()

            print("Save button clicked")

            time.sleep(3)

            return True

        except Exception as e:

            print("Failed to click Save button")
            print("Error:", e)

            return False

    def dismiss_google_save_password_popup(self):

        try:

            print("Checking Google Save Password popup...")

            never_button = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(
                    self.NEVER_BUTTON
                )
            )

            print("Google Save Password popup detected")

            never_button.click()

            print("Never button clicked")

            time.sleep(2)

            print("Google Save Password popup dismissed")

            return True

        except TimeoutException:

            print(
                "Google Save Password popup not displayed - Continuing"
            )

            return True

        except Exception as e:

            print("Error handling Google Save Password popup")
            print("Error:", e)

            return True

    def navigate_up(self):

        try:

            back_button = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(
                    self.NAVIGATE_UP
                )
            )

            back_button.click()

            print("Navigate Up clicked")

            time.sleep(2)

            return True

        except Exception as e:

            print("Failed to navigate up")
            print("Error:", e)

            return False

    def add_or_update_vehicle(
        self,
        vehicle_id,
        vehicle_label,
        server_password,
        module_password
    ):

        try:

            # ==================================================
            # STEP 1: Check whether existing vehicle is openable
            # ==================================================

            existing_vehicle = self.open_existing_vehicle()

            # ==================================================
            # STEP 2: If no existing vehicle, click Add
            # ==================================================

            if not existing_vehicle:

                if not self.open_add_vehicle():

                    return False

            # ==================================================
            # STEP 3: Enter / Update Vehicle Details
            # ==================================================

            if not self.enter_vehicle_details(
                vehicle_id,
                vehicle_label,
                server_password,
                module_password
            ):

                return False

            # ==================================================
            # STEP 4: Save
            # ==================================================

            if not self.click_save():

                return False

            print("Vehicle details saved successfully")

            # ==================================================
            # STEP 5: Google Password Manager
            # ==================================================

            self.dismiss_google_save_password_popup()

            # ==================================================
            # STEP 6: Navigate Back
            # ==================================================

            if not self.navigate_up():

                return False

            print("Vehicle operation completed")

            return True

        except Exception as e:

            print("Failed to add/update vehicle")
            print("Error:", e)

            return False

    # Keep backward compatibility with your existing test
    def add_vehicle(
        self,
        vehicle_id,
        vehicle_label,
        server_password,
        module_password
    ):

        return self.add_or_update_vehicle(
            vehicle_id=vehicle_id,
            vehicle_label=vehicle_label,
            server_password=server_password,
            module_password=module_password
        )

