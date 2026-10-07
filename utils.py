from openpyxl import load_workbook

workbook = load_workbook("data/SuperMart_Raw_Data.xlsx")
print("Excel file loaded successfully!")

Customers_sheet = workbook["customers"]
employees_sheet = workbook["employees"]
products_sheet = workbook["products"]
orders_sheet = workbook["orders"]