# 📄 File: Utils/excel_reader.py

import pandas as pd
import os

class ExcelReader:
    def __init__(self, filename='Indonesia administrative boundaries.xlsx'):
        self.file_path = os.path.join(os.path.dirname(__file__), '..', 'Data', filename)

    def read_sheet(self, sheet_name):
        try:
            df = pd.read_excel(self.file_path, sheet_name=sheet_name)
            print(f"✅ Đọc sheet '{sheet_name}' thành công.")
            return df
        except FileNotFoundError:
            print(f"❌ Không tìm thấy file Excel: {self.file_path}")
        except ValueError as e:
            print(f"❌ Lỗi khi đọc sheet: {e}")
