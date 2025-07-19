from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:
    def __init__(self, browser='chrome'):
        self.browser = browser.lower()

    def create_driver(self):
        if self.browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            service = Service(ChromeDriverManager().install())
            return webdriver.Chrome(service=service, options=options)
        else:
            raise Exception(f"{self.browser} is not supported")
