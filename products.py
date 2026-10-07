from utils import products_sheet,workbook
from logger import log_activity

def view_products():
    print("ProductID\tProduct\t\tPrice")
    print("-" * 40)

    for row in products_sheet.iter_rows(min_row=2, max_row=6, values_only=True):
        print(row[0], "\t", row[1], "\t", row[3])

def product_search():
    product_name = input("Enter Product Name:- ")
   
    for row in products_sheet.iter_rows(min_row=2, values_only=True):
        if row[1] == product_name:
            print("Product Found! ")
            print("Product ID :", row[0])
            print("Product",row[1])
            print("Category", row[2])
            break
    else :
         print("Product Not Found")

def update_product_stock():

    product_id = input("Enter Product ID: ")
    try:
        new_stock = int(input("Enter New Stock: "))
    except ValueError:
        print("\nInvalid Input! Please enter a Number.")
        print("\nPress Enter To Retuen To Main Menu...")
        return
    
    for row in products_sheet.iter_rows(min_row=2):

        if row[0].value == product_id:
            row[4].value = new_stock

            workbook.save("data/SuperMart_Raw_Data.xlsx")
            print("\nStock Updated Successfully!")
            input("\nPress Enter to return to Main Menu...")
            return
    else:
        print("\nProduct Not Found!")
        input("\nPress Enter to return to Main Menu...")

def restock_Product():
    product_id = input("Enter Product ID:- ")
    try:
        added_stock = int(input("Enter Your Added Stock:- "))
    except ValueError:
        print("\nInvalid Input! Please A Number.")
        log_activity("Invalid input for added stock.")
        print("\nPress Enter TO Return TO Main Menu...")
        return

    if added_stock <= 0:
        print("\nAdded Stock Must be Greater Then 0!")
        input("\nPress Enter TO Return To Main Menu...")
        return

    for row in products_sheet.iter_rows(min_row=2):
        if row[0].value == product_id:
            product_name = row[1].value
            current_stock = row[4].value
            row[4].value = row[4].value + added_stock
            workbook.save("data/SuperMart_Raw_Data.xlsx")
            log_activity(f"Product restocked: {product_name}, Quantity: {added_stock}")
            print("\nStock Restock Successfully!")
            print("New Stock :", row[4].value)
            input("\nPress Enter To Return To Main Menu...")
            return

    print("\nProduct Not Found!")
    log_activity("Product not found.")
    input("\nPress Enter To Return To Main Menu...")

def low_stock_report():
    print("Product\t\tStock")
    print("-" * 25)

    found = False

    for row in products_sheet.iter_rows(min_row=2, values_only=True):
        if row[4] <= 55:
            print(row[1], "\t", row[4])
            found = True
    if not found:
        print("No low stock products found!")
        input("\nPress Enter to Return to Main Menu.. ")

def out_of_stock():
    print("Product\t\tStock")
    print("-"*25)

    found = False

    for row in products_sheet.iter_rows(min_row=2, values_only=True):
        if row[0] == 0:
            print(row[1], "\t", row[4])
            found = True
    if not found:
        print("No Out Of Stock Found")
        input("\nPress Enter to Return to Main Menu.. ")

def delete_product():
    productid = input("Enter ProductID To Delete:- ")

    for row in products_sheet.iter_rows(min_row=2):
        if row[0].value == productid:
            products_sheet.delete_rows(row[0].row)

            workbook.save("data/SuperMart_Raw_Data.xlsx")
            print("nProduct Deleted Successfully!")
            print("/nPress Enter To Return To Main Menu...")
            return
    else:
        print("Product Not Found")
        print("\nPress Enter TO Return To Main Menu...")