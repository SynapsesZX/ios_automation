from page_object.base_page import BasePage
import locators.settings


class SettingsIcon(BasePage):

    def click_settings_icon(self):
        self.wait_and_click(locators.settings.settings_icon)
