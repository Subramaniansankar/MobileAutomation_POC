from appium import webdriver
from appium.options.android import UiAutomator2Options


def get_driver():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"

    options.device_name = "Android Device"
    options.udid = "ZF6525JTJS"

    options.app_package = "com.openvehicles.OVMS"
    options.app_activity = "com.openvehicles.OVMS.ui2.MainActivityUI2"

    options.no_reset = True

    options.set_capability("autoGrantPermissions", True)
    options.set_capability("adbExecTimeout", 120000)
    options.set_capability("uiautomator2ServerInstallTimeout", 120000)
    options.set_capability("uiautomator2ServerLaunchTimeout", 120000)
    options.set_capability("newCommandTimeout", 300)

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    driver.implicitly_wait(10)

    return driver