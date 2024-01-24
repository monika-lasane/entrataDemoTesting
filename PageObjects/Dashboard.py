from selenium.webdriver.common.by import By


class Dashboard:
    def __init__(self, driver):
        self.driver = driver

    logo = (By.ID, "Layer_1")
    resources = (By.LINK_TEXT, "Resources")
    watch_demo_btn = (By.XPATH, "(//a[contains(text(), 'Watch Demo')])[1]")
    sign_in_btn = (By.LINK_TEXT, "Sign In")

    def get_logo(self):
        return self.driver.find_element(*Dashboard.logo)

    def watch_demo(self):
        return self.driver.find_element(*Dashboard.watch_demo_btn)

    def sign_in(self):
        return self.driver.find_element(*Dashboard.sign_in_btn)

    def navigate_resource(self):
        return self.driver.find_element(*Dashboard.resources)
