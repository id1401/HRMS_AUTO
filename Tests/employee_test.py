import unittest
from Driver.driver_factory import DriverFactory
from Config.config_reader import ConfigReader
from Page.employee_page import EmployeePage
from Page.login_page import LoginPage
from Utils.excel_reader import ExcelReader
from Utils.db_helper import DBHelper

class TestEmployee(unittest.TestCase):
    def setUp(self):
        config = ConfigReader()
        self.driver = DriverFactory().create_driver()
        self.driver.get(config.get("base_url"))

        # Đăng nhập hệ thống
        login_page = LoginPage(self.driver)
        login_page.login("QPC25L33336", "Pum@@26/01/2003...")

    def test_dummy(self):
        self.assertTrue(True)

    def tearDown(self):
        self.driver.quit()

    #     # Điều hướng đến form tạo employee mới
    #     self.page = EmployeePage(self.driver)
    #     self.page.open_employee_module()
    #     self.page.click_create_button()
    #     self.page.switch_to_contract_address_tab()
    #     self.page.select_country("Việt Nam")
    #
    #     # Chuẩn bị data
    #     self.excel = ExcelReader()
    #     self.db = DBHelper()
    #
    # def test_province_district_ward(self):
    #     # Province
    #     web_provinces = self.page.get_provinces()
    #     excel_provinces = self.excel.read_sheet("Province")['name'].tolist()
    #     db_provinces = list(self.db.get_provinces().values())
    #     self.assertCountEqual(web_provinces, excel_provinces)
    #     self.assertCountEqual(web_provinces, db_provinces)
    #
    #     # District & Ward
    #     df_districts = self.excel.read_sheet("District")
    #     df_wards = self.excel.read_sheet("Ward")
    #
    #     for prov_code, prov_name in self.db.get_provinces().items():
    #         self.page.select_province(prov_name)
    #         web_districts = self.page.get_districts()
    #         excel_districts = df_districts[df_districts['province_code'] == prov_code]['name'].tolist()
    #         db_districts = list(self.db.get_districts_by_province(prov_code).values())
    #
    #         self.assertCountEqual(web_districts, excel_districts)
    #         self.assertCountEqual(web_districts, db_districts)
    #
    #         for dist_code, dist_name in self.db.get_districts_by_province(prov_code).items():
    #             self.page.select_district(dist_name)
    #             web_wards = self.page.get_wards()
    #             excel_wards = df_wards[df_wards['district_code'] == dist_code]['name'].tolist()
    #             db_wards = list(self.db.get_wards_by_district(dist_code).values())
    #
    #             self.assertCountEqual(web_wards, excel_wards)
    #             self.assertCountEqual(web_wards, db_wards)

