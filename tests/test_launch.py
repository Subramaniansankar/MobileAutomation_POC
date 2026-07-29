from pages.launch_page import LaunchPage


class TestLaunch:

    def test_verify_application_launch(self, driver):

        launch = LaunchPage(driver)

        # Handle popups if they appear
        launch.dismiss_version_popup()
        launch.allow_location_permission()

        # Verify dashboard loaded
        assert launch.verify_app_launched()