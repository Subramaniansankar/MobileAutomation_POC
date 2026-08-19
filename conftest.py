import pytest
from utilities.driver_factory import get_driver


# =========================================================
# Command Line Option
# =========================================================

def pytest_addoption(parser):
    parser.addoption(
        "--platform",
        action="store",
        default="android",
        help="Platform: android or ios"
    )


# =========================================================
# Driver Fixture
# =========================================================

@pytest.fixture
def driver(request):

    platform = request.config.getoption("--platform")

    driver = get_driver(platform)

    yield driver

    driver.quit()


# =========================================================
# Test Result Counter
# =========================================================

test_results = {
    "passed": 0,
    "failed": 0,
    "skipped": 0
}


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    # Count only actual test execution result
    if report.when == "call":

        if report.passed:
            test_results["passed"] += 1

        elif report.failed:
            test_results["failed"] += 1

        elif report.skipped:
            test_results["skipped"] += 1


# =========================================================
# HTML Report Summary
# =========================================================

def pytest_html_results_summary(prefix, summary, postfix):

    passed = test_results["passed"]
    failed = test_results["failed"]
    skipped = test_results["skipped"]

    total = passed + failed + skipped

    if total > 0:
        pass_percentage = (passed / total) * 100
        fail_percentage = (failed / total) * 100
    else:
        pass_percentage = 0
        fail_percentage = 0

    prefix.extend([
        "<h2>OVMS Mobile Automation Test Summary</h2>",

        "<table style='border-collapse: collapse; width: 60%;'>",

        "<tr>"
        "<th style='border:1px solid #ddd;padding:10px;'>Total Tests</th>"
        "<th style='border:1px solid #ddd;padding:10px;'>Passed</th>"
        "<th style='border:1px solid #ddd;padding:10px;'>Failed</th>"
        "<th style='border:1px solid #ddd;padding:10px;'>Skipped</th>"
        "<th style='border:1px solid #ddd;padding:10px;'>Pass %</th>"
        "<th style='border:1px solid #ddd;padding:10px;'>Fail %</th>"
        "</tr>",

        "<tr>"
        f"<td style='border:1px solid #ddd;padding:10px;text-align:center;'>{total}</td>"
        f"<td style='border:1px solid #ddd;padding:10px;text-align:center;'>{passed}</td>"
        f"<td style='border:1px solid #ddd;padding:10px;text-align:center;'>{failed}</td>"
        f"<td style='border:1px solid #ddd;padding:10px;text-align:center;'>{skipped}</td>"
        f"<td style='border:1px solid #ddd;padding:10px;text-align:center;'>{pass_percentage:.2f}%</td>"
        f"<td style='border:1px solid #ddd;padding:10px;text-align:center;'>{fail_percentage:.2f}%</td>"
        "</tr>",

        "</table>",
        "<br>"
    ])