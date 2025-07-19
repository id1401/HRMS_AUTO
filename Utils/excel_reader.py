import pandas as pd
import os

class ExcelReader:
    def __init__(self, filename='expected_location_data.xlsx'):
        self.file_path = os.path.join(os.path.dirname(__file__), '..', 'Data', filename)

    def read_sheet(self, sheet_name):
        return pd.read_excel(self.file_path, sheet_name=sheet_name)
