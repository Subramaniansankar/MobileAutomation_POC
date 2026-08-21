from appium import webdriver
from appium.options.ios import XCUITestOptions


def get_driver():

    options = XCUITestOptions()

    options.platform_name = "iOS"
    options.automation_name = "XCUITest"

    options.device_name = "iPhone XS Max"
    options.udid = "00008020-00051DD83481002E"

    # Launch installed app
    options.bundle_id = "com.openvehicles.ovms"

    # Signing details
    options.xcode_org_id = "T8Q45M2ARM"
    options.xcode_signing_id = "Apple Development"

    # Reuse WebDriverAgent
    options.use_prebuilt_wda = True
    options.use_new_wda = False
    options.show_xcode_log = True

    # Don't reinstall the app every run
    options.no_reset = True

    options.new_command_timeout = 300

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    driver.implicitly_wait(10)

    return driver