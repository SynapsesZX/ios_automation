from page_object.ios_settings import SettingsIcon
import pytest


@pytest.mark.settings_icon_regression
class TestSettings:
    def test_settings_access(self, driver):
        user = SettingsIcon(driver)
        user.click_settings_icon()
