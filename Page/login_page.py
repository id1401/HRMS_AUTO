from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, '//*[@id=":r0:"]')
        self.password_input = (By.XPATH, '//*[@id=":r1:"]')
        self.login_button = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/button')

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
