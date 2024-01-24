# Import necessary modules and classes
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Import PageObjects and Utilities
from PageObjects.Dashboard import Dashboard
from Utilities.BaseClass import BaseClass


# Define a test class that inherits from BaseClass
class TestResources(BaseClass):

    # Setup method to create a shared instance of the Dashboard class before each test method
    def setup_method(self, method):
        # Instantiate the Dashboard class and assign it to the shared instance variable
        self.dashboard = Dashboard(self.driver)

    # Test method to check if the logo is present
    def test_is_logo_present(self):
        # Check if a confirmation button is present and click it if found
        if self.driver.find_element(By.ID, "rcc-confirm-button"):
            self.driver.find_element(By.ID, "rcc-confirm-button").click()

        # Assert that the logo is displayed on the page using the shared Dashboard instance
        assert self.dashboard.get_logo().is_displayed()

    # Test method to click the resource button and check the URL
    def test_click_resource_button(self):
        # Navigate to the resource page and click on the resource button using the shared Dashboard instance
        self.dashboard.navigate_resource().click()

        # Set up a WebDriverWait instance for explicit wait
        wait = WebDriverWait(self.driver, 10)

        # Wait until an h2 element is present on the page
        wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "h2")))

        # Assert that the current URL matches the expected URL
        assert self.driver.current_url == "https://www.entrata.com/"

    # Test method to click the watch demo button and check the URL
    def test_watch_demo(self):
        # Check if the watch demo button is displayed and click it if found using the shared Dashboard instance
        if self.dashboard.watch_demo().is_displayed():
            self.dashboard.watch_demo().click()

        # Assert that the current URL matches the expected URL
        assert self.driver.current_url == "https://go.entrata.com/watch-demo.html"

        # Navigate back to the previous page
        self.driver.back()

    # Test method to click the sign-in button and check the URL
    def test_sign_in(self):
        # Check if the sign-in button is displayed and click it if found using the shared Dashboard instance
        if self.dashboard.sign_in().is_displayed():
            self.dashboard.sign_in().click()

        # Assert that the current URL matches the expected URL
        assert self.driver.current_url == "https://www.entrata.com/sign-in"
