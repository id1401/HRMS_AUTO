import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="pandas only supports SQLAlchemy.*")
import os
import sys
import pandas as pd

# 👉 Cấu hình hiển thị đầy đủ dữ liệu không bị rút gọn
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', None)

# 👉 Thêm thư mục gốc vào sys.path để import module tự định nghĩa
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Utils.excel_reader import ExcelReader
from Utils.db_helper import DBHelper


def compare_provinces(reader, db):
    print("\n🔍 So sánh dữ liệu TỈNH (Sheet1)...")
    try:
        df_excel = reader.read_sheet("Sheet1")
        df_excel = df_excel[["ProvinceName_in", "ProvinceName_En", "RefGeo"]].astype(str)
        print(f"📄 Số dòng Excel (Tỉnh): {len(df_excel)}")
    except Exception as e:
        print(f"❌ Lỗi đọc sheet tỉnh: {e}")
        return

    query = """
        SELECT 
            ProvinceName AS ProvinceName_in,
            ProvinceNameENG AS ProvinceName_En,
            RefProvinceCode AS RefGeo
        FROM HRMS_Testing.dbo.Province
        WHERE CountryId = 4
        ORDER BY ProvinceId
    """
    try:
        df_sql = db.read_sql(query).astype(str)
        print(f"🗃️ Số dòng SQL (Tỉnh): {len(df_sql)}")
    except Exception as e:
        print(f"❌ Lỗi truy vấn SQL tỉnh: {e}")
        return

    diff = df_excel.compare(df_sql, result_names=("Excel", "SQL"))
    if diff.empty:
        print("✅ Dữ liệu TỈNH khớp.")
        print(df_excel)
    else:
        print("❌ Dữ liệu TỈNH không khớp:")
        diff = diff.reset_index()
        diff.columns = [f"{col[0]}_{col[1]}" if isinstance(col, tuple) else col for col in diff.columns]
        diff.to_excel("Province_Compare_Diff.xlsx", index=False)
        print(diff)
        print("📁 Đã ghi khác biệt vào 'Province_Compare_Diff.xlsx'")


def compare_districts(reader, db):
    print("\n🔍 So sánh dữ liệu HUYỆN (Sheet2)...")
    try:
        df_excel = reader.read_sheet("Sheet2")
        df_excel = df_excel[["Regency/City_Code", "Regency/City_IN", "Regency/City_ENG", "Pro_Code"]].astype(str)
        df_excel.columns = ["DistrictCode", "DistrictName", "DistrictNameENG", "RefProvinceCode"]
        print(f"📄 Số dòng Excel (Huyện): {len(df_excel)}")
    except Exception as e:
        print(f"❌ Lỗi đọc sheet huyện: {e}")
        return

    query = """
        SELECT 
            d.DistrictCode,
            d.DistrictName,
            d.DistrictNameENG,
            p.RefProvinceCode
        FROM HRMS_Testing.dbo.District d
        JOIN HRMS_Testing.dbo.Province p ON d.ProvinceId = p.ProvinceId
        WHERE d.CountryId = 4
        ORDER BY d.DistrictId
    """
    try:
        df_sql = db.read_sql(query).astype(str)
        # Cắt tiền tố "ID" nếu có
        df_sql["DistrictCode"] = df_sql["DistrictCode"].str.replace("^ID", "", regex=True)
        print(f"🗃️ Số dòng SQL (Huyện): {len(df_sql)}")
    except Exception as e:
        print(f"❌ Lỗi truy vấn SQL huyện: {e}")
        return

    diff = df_excel.compare(df_sql, result_names=("Excel", "SQL"))
    if diff.empty:
        print("✅ Dữ liệu HUYỆN khớp.")
        print(df_excel)
    else:
        print("❌ Dữ liệu HUYỆN không khớp:")
        diff = diff.reset_index()
        diff.columns = [f"{col[0]}_{col[1]}" if isinstance(col, tuple) else col for col in diff.columns]
        diff.to_excel("District_Compare_Diff.xlsx", index=False)
        print(diff)
        print("📁 Đã ghi khác biệt vào 'District_Compare_Diff.xlsx'")



def compare_wards(reader, db):
    print("\n🔍 So sánh dữ liệu XÃ (Sheet3)...")
    try:
        df_excel = reader.read_sheet("Sheet3")
        df_excel = df_excel[["Code", "Kecamatan_Name", "Kecamatan_ENG", "Ref_KAB_code", "Ref_Prov_code"]].astype(str)
        df_excel.columns = ["WardCode", "WardName", "WardNameENG", "RefDistrictCode", "RefProvinceCode"]
        print(f"📄 Số dòng Excel (Xã): {len(df_excel)}")
        print(df_excel.to_string(index=False))
    except Exception as e:
        print(f"❌ Lỗi đọc sheet xã: {e}")
        return

    query = """
        SELECT 
            w.WardCode,
            w.WardName,
            w.WardNameENG,
            d.RefDistrictCode,
            p.RefProvinceCode
        FROM HRMS_Testing.dbo.Ward w
        JOIN HRMS_Testing.dbo.District d ON w.DistrictId = d.DistrictId
        JOIN HRMS_Testing.dbo.Province p ON w.ProvinceId = p.ProvinceId
        WHERE w.CountryId = 4
        ORDER BY w.WardId
    """
    try:
        df_sql = db.read_sql(query).astype(str)
        df_sql["WardCode"] = df_sql["WardCode"].str.replace("^ID-", "", regex=True)  # Nếu có tiền tố ID
        print(f"🗃️ Số dòng SQL (Xã): {len(df_sql)}")
        print(df_sql.to_string(index=False))
    except Exception as e:
        print(f"❌ Lỗi truy vấn SQL xã: {e}")
        return

    diff = df_excel.compare(df_sql, result_names=("Excel", "SQL"))
    if diff.empty:
        print("✅ Dữ liệu XÃ khớp.")
    else:
        print("❌ Dữ liệu XÃ không khớp:")
        diff = diff.reset_index()
        diff.columns = [f"{col[0]}_{col[1]}" if isinstance(col, tuple) else col for col in diff.columns]
        diff.to_excel("Ward_Compare_Diff.xlsx", index=False)
        print(diff.to_string(index=False))
        print("📁 Đã ghi khác biệt vào 'Ward_Compare_Diff.xlsx'")

def main():
    reader = ExcelReader()
    db = DBHelper()

    try:
        compare_provinces(reader, db)
        compare_districts(reader, db)
        compare_wards(reader, db)
    finally:
        db.close()
        print("🔒 Đã đóng kết nối DB.")


if __name__ == "__main__":
    main()
