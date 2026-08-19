from pages.ios.message_page import MessagePage


class TestMessage:

    def test_send_message(self, driver):

        message = MessagePage(driver)

        message.send_message("Hello from iOS Appium Automation")