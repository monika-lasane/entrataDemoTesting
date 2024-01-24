from selenium.webdriver.common.by import By


class ResourcesPage:
    def __init__(self, driver):
        self.driver = driver

    resources = (By.LINK_TEXT, "Resources")

    def navigate_resource(self):
        return self.driver.find_element(*Dashboard.resources)
