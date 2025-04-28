import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions

import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions


@pytest.fixture
def driver():
    # Create options for the iOS test
    options = XCUITestOptions()
    options.platform_name = "iOS"  # Removed the trailing comma
    options.platform_version = "17.0.3"  # Removed the trailing comma
    options.device_name = "iPhone Synapses"  # Removed the trailing comma
    options.automation_name = "XCUITest"  # Removed the trailing comma
    options.udid = "00008101-001C29560E45001E"  # Removed the trailing comma

    # Initialize the WebDriver instance
    driver = webdriver.Remote("http://169.254.81.47:4723", options=options)

    yield driver  # This will yield the driver to be used in the test

    # Quit the driver after the test is complete
    driver.quit()
