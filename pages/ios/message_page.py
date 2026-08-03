from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MessagePage:

    def __init__(self, driver):
        self.driver = driver

    MESSAGE_MENU = (
        AppiumBy.ACCESSIBILITY_ID,
        "Messages"
    )

    MESSAGE_TEXTBOX = (
        AppiumBy.CLASS_NAME,
        "XCUIElementTypeTextView"
    )

    SEND_BUTTON = (
        AppiumBy.IOS_PREDICATE,
        "name == 'Send'"
    )

    def send_message(self, message):

        # Open Messages screen
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.MESSAGE_MENU)
        ).click()

        print("✅ Messages screen opened")

        # Wait for the text box
        textbox = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.MESSAGE_TEXTBOX)
        )

        textbox.click()
        textbox.send_keys(message)

        print(f"✅ Message entered: {message}")

        # Click Send
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.SEND_BUTTON)
        ).click()

        print("✅ Send button clicked")