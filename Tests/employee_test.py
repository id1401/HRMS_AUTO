import time
import unittest
from Driver.driver_factory import DriverFactory
from Config.config_reader import ConfigReader
from Page.employee_page import EmployeePage
from Page.login_page import LoginPage

class TestEmployee(unittest.TestCase):
    def setUp(self):
        config = ConfigReader()
        self.driver = DriverFactory().create_driver()
        self.driver.get(config.get("base_url"))
        login_page = LoginPage(self.driver)
        login_page.login("BXZ252145961", "Duyen@@26/01/2003...")
        self.page = EmployeePage(self.driver)
        self.page.open_employee_module()
        self.page.click_create_button()
        time.sleep(5)
        self.page.switch_to_contract_address_tab()
        time.sleep(5)
        self.page.select_country()
        time.sleep(5)
        self.page.click_country()
        time.sleep(5)
        self.page.select_province()
        time.sleep(5)





        self.page.click_province()
        time.sleep(5)
        self.page.select_district()
        time.sleep(5)
        self.page.click_regency()
        time.sleep(5)
        self.page.select_ward()
        time.sleep(5)
        self.page.click_ward()
        time.sleep(5)

    def test_dummy(self):
        self.assertTrue(True)

    def tearDown(self):
        self.driver.quit()



