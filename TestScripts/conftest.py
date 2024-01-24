import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None

@pytest.fixture(scope="class")
def setup(request):
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    service = Service(r'C:\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    driver.get("https://entrata.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield

    driver.close()




