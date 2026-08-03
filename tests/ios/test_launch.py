from pages.ios.launch_page import LaunchPage


class TestLaunch:

    def test_verify_application_launch(self, driver):

        launch_page = LaunchPage(driver)

        # Handle version popup if displayed
        launch_page.dismiss_version_popup()

        # Handle location permission if displayed
        launch_page.allow_location_permission()

        # Verify app launched successfully
        assert launch_page.verify_app_launched()


    