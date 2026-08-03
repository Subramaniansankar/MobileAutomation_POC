import pytest
from utilities.driver_factory import get_driver


def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="Platform: android or ios"
    )


@pytest.fixture
def driver(request):

    platform = request.config.getoption("--platform")

    driver = get_driver(platform)

    yield driver

    driver.quit()