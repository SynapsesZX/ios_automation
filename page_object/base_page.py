from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Base page for IOS

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_click(self, locator, timeout=10):
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

    def send_keys(self, locator, value):
        """
               Hides the keyboard (if visible), waits for the element specified by the locator to be present,
               then sends the given value to it.

               Parameters:
               locator (tuple): A tuple containing the strategy to locate the element and the locator value,
                                e.g., (By.XPATH, "//input[@id='username']")
               value (str): The string value to send to the located element.
        """
        self.driver.hide_keyboard()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        element.send_keys(value)

    def check_element_text(self, locator, text):
        """
             Waits for an element to be present, retrieves its text, and asserts that it matches the expected text.

             Parameters:
             locator (tuple): A tuple specifying the strategy and locator for the element,
                              e.g., (By.CLASS_NAME, "success-message")
             text (str): The expected text to be matched against the element's actual text.

             Raises:
             AssertionError: If the actual text does not match the expected text.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        actual_text = element.text
        assert actual_text == text

    def check_element_attribute(self, locator, attribute, attribute_value):
        """
            Parameters:
            locator (tuple): A tuple specifying the strategy and locator for the element,
                             e.g., (By.ID, "submit-button")
            attribute (str): The name of the attribute to check on the element,
                             e.g., "type", "value", "class".
            attribute_value (str): The expected value of the specified attribute.

            Raises:
            AssertionError: If the actual attribute value does not match the expected value.
        """
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        element = element.get_attribute(attribute)
        assert element == attribute_value

    def press_back_button(self):
        """
          Simulates pressing the 'Back' button on the device using Appium.
        """
        self.driver.back()

    def check_if_element_is_not_displayed(self, locator):
        """
        Waits until the given element is no longer visible on the screen.

        Parameters:
        ----------
        locator : tuple
            A tuple representing the locator strategy and locator value.
            Example: (By.ID, "com.example:id/error_popup") or (By.XPATH, "//android.widget.TextView[@text='Error']")

        Raises:
        ------
        Exception
            If the element is still displayed after the timeout period.
        """
        try:

            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(locator)
            )
            print("element is not displayed.")
        except TimeoutException:
            raise Exception("element is still displayed")
