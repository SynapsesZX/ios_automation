from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def wait_and_click(self,locator, timeout=10):
        """
    Waits for an element to be clickable and then clicks it.

    :param driver: Appium WebDriver instance
    :param locator: Locator (tuple) to find the element (e.g., (By.ACCESSIBILITY_ID, "loginButton"))
    :param timeout: Maximum wait time in seconds (default is 30 seconds)
    :return: None
        """

    # Wait for the element to be clickable
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    # Perform the click action
        element.click()
