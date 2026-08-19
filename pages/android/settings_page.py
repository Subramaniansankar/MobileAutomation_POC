from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class SettingsPage:

    # =========================================================
    # LOCATORS
    # =========================================================

    ADD_BUTTON = (
        AppiumBy.ID,
        "com.openvehicles.OVMS:id/mi_add"
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

    # =========================================================
    # CONSTRUCTOR
    # =========================================================

    def __init__(self, driver):
        self.driver = driver

    # =========================================================
    # CLICK + ICON
    # =========================================================

    def open_add_vehicle(self):

        try:

            print("Waiting for + Add Vehicle button...")

            add_button = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.element_to_be_clickable(
                    self.ADD_BUTTON
                )
            )

            add_button.click()

            print("+ Add Vehicle button clicked")

            time.sleep(2)

            return True

        except Exception as e:

            print("Failed to open Add Vehicle")
            print("Error:", e)

            return False

    # =========================================================
    # ENTER VEHICLE DETAILS
    # =========================================================

    def enter_vehicle_details(
        self,
        vehicle_id,
        vehicle_label,
        server_password,
        module_password
    ):

        try:

            # -------------------------------------------------
            # Vehicle ID
            # -------------------------------------------------

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

            print("Vehicle ID entered:", vehicle_id)

            # -------------------------------------------------
            # Vehicle Label
            # -------------------------------------------------

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

            print("Vehicle Label entered:", vehicle_label)

            # -------------------------------------------------
            # Server Password
            # -------------------------------------------------

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

            print("Server Password entered")

            # -------------------------------------------------
            # Module/SMS Password
            # -------------------------------------------------

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

            print("Module/SMS Password entered")

            return True

        except Exception as e:

            print("Failed to enter vehicle details")
            print("Error:", e)

            return False

    # =========================================================
    # CLICK SAVE
    # =========================================================

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

    # =========================================================
    # GOOGLE PASSWORD MANAGER POPUP
    # =========================================================

    def dismiss_google_save_password_popup(self):

        try:

            print("Checking Google Save Password popup...")

            never_button = WebDriverWait(
                self.driver,
                5
            ).until(
                EC.element_to_be_clickable(
                    self.NEVER_BUTTON
                )
            )

            print("Google Save Password popup detected")

            never_button.click()

            print("Never button clicked")

            time.sleep(2)

            return True

        except TimeoutException:

            print(
                "Google Save Password popup not displayed - Continuing"
            )

            return True

        except Exception as e:

            print(
                "Error while handling Google Save Password popup"
            )

            print("Error:", e)

            # Popup is optional, so don't fail test
            return True

    # =========================================================
    # NAVIGATE UP
    # =========================================================

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

    # =========================================================
    # ADD NEW VEHICLE
    # =========================================================

    def add_new_vehicle(
        self,
        vehicle_id,
        vehicle_label,
        server_password,
        module_password
    ):

        try:

            print("==============================================")
            print("STARTING ADD NEW VEHICLE FLOW")
            print("==============================================")

            # -------------------------------------------------
            # STEP 1 - Click + icon
            # -------------------------------------------------

            if not self.open_add_vehicle():

                print("Unable to click + icon")

                return False

            print("Add Vehicle screen opened")

            # -------------------------------------------------
            # STEP 2 - Enter vehicle details
            # -------------------------------------------------

            if not self.enter_vehicle_details(
                vehicle_id=vehicle_id,
                vehicle_label=vehicle_label,
                server_password=server_password,
                module_password=module_password
            ):

                print("Unable to enter vehicle details")

                return False

            # -------------------------------------------------
            # STEP 3 - Save
            # -------------------------------------------------

            if not self.click_save():

                print("Unable to save vehicle")

                return False

            # -------------------------------------------------
            # STEP 4 - Handle Google Password popup
            # -------------------------------------------------

            self.dismiss_google_save_password_popup()

            print("==============================================")
            print("NEW VEHICLE SAVED SUCCESSFULLY")
            print("==============================================")

            return True

        except Exception as e:

            print("Failed to add new vehicle")
            print("Error:", e)

            return False