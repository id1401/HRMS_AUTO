import configparser

import pyodbc

from Config.config_reader import ConfigReader


class DBHelper:
    def __init__(self, env='Testing'):
        config = ConfigReader(env)
        self.connection = pyodbc.connect(
            f"DRIVER={{SQL Server}};"
            f"SERVER=172.17.100.110;"
            f"DATABASE={config.get('db_name')};"
            f"UID={config.get('db_user')};"
            f"PWD={config.get('db_password')};"
        )
        self.cursor = self.connection.cursor()
        self.company_id = 218

    def get_provinces(self):
        self.cursor.execute("""
            SELECT ProvinceCode AS code, ProvinceName AS name
            FROM Province
            WHERE IsActive = 1 AND CompanyId = ?
        """, self.company_id)
        return {row.code: row.name for row in self.cursor.fetchall()}

    def get_districts_by_province(self, province_id):
        self.cursor.execute("""
            SELECT DistrictCode AS code, DistrictName AS name
            FROM District
            WHERE IsActive = 1 AND ProvinceId = ? AND CompanyId = ?
        """, province_id, self.company_id)
        return {row.code: row.name for row in self.cursor.fetchall()}

    def get_wards_by_district(self, district_id):
        self.cursor.execute("""
            SELECT WardCode AS code, WardName AS name
            FROM Ward
            WHERE IsActive = 1 AND DistrictId = ? AND CompanyId = ?
        """, district_id, self.company_id)
        return {row.code: row.name for row in self.cursor.fetchall()}
