# This is standalone file that I have written for my understanding

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(r"C:\Users\lenovo\PycharmProjects\entrataTesting\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)
# request.cls.driver = driver
driver.get("https://entrata.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT, "Resources").click()
