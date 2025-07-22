import pyodbc
import pandas as pd

class DBHelper:
    def __init__(self):
        self.server = '192.168.1.248'
        self.database = 'HRMS_Testing'
        self.username = 'user_hrms_readonly'
        self.password = '14J7kndO#W19'

        self.connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={self.server};DATABASE={self.database};"
            f"UID={self.username};PWD={self.password}"
        )

        try:
            self.connection = pyodbc.connect(self.connection_string)
            print("✅ Đã kết nối DB.")
        except Exception as e:
            print(f"❌ Lỗi kết nối DB: {e}")
            self.connection = None

    def read_sql(self, query):
        if self.connection:
            return pd.read_sql(query, self.connection)
        else:
            raise Exception("Không có kết nối tới cơ sở dữ liệu.")

    def close(self):
        if self.connection:
            self.connection.close()
            print("🔒 Đã đóng kết nối DB.")
