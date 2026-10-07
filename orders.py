from utils import orders_sheet, Customers_sheet, products_sheet, workbook
from logger import log_activity

def view_order():
    print("OrderID\tCustomerID\tEmployeeId\tProductID\tQuantity")
    print("-"*45)

    for row in orders_sheet.iter_rows(min_row=2, values_only=True):
        print(row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t", row[4])
    input("\n Press Enter to Return to Main Menu...")

def search_order():
    order_id = input("Enter your Order ID: ")

    for row in orders_sheet.iter_rows(min_row=2, values_only=True):
        if row[0] == order_id:
            print("\n Order Found! ")
            print("OrderId :", row[0])
            print("CustomerID :", row[1])
            print("EmployeeID :", row[2])
            print("ProductID :", row[3])
            print("QuantityID :", row[4])
            input("\nPress Enter to Return To Main Menu...")
            return
    print("Order Not Found!")
    log_activity("Order not found.")    
    input("\nPress Enter to return to Main Menu...")

def add_new_order():
    order_id = input("Enter your Order ID:")
    try:
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("\nInvalid Input! Please Enter A Number.")
        log_activity("Invalid input for order quantity.")       
        print("\nPress Enter To Return TO Main Menu...")
        return
    orders_sheet.append([order_id, customer_id, product_id, quantity])

    for row in products_sheet.iter_rows(min_row=2, values_only=True):   
        if row[0].value == order_id:
            print("\nOrder ID Already Exists!")
            input("\nPress EnterTo Return To Main Menu...")
            return

    customer_id = input("Enter Customer ID:- ")
    product_id = input("Enter Product ID:- ")

            

    workbook.save("data/SuperMart_Raw_Data.xlsx")
    print("\nOrder Added Successfully! ")
    print("Stock updated Successfully!")
    input("\nPress Enter to Return to Main Menu... ")

def delete_order():
    order_id = input("Enter Order ID to Delete: ")

    for row in orders_sheet.iter_rows(min_row=2):
        if row[0].value == order_id:
            orders_sheet.delete_rows(row[0].row)

            workbook.save("data/SuperMart_Raw_Data.xlsx")
            print("\nOrder Deleted Successfully!")
            input("\nPress Enter to Return to Main Menu...")
            return

    print("\nOrder Not Found!")
    input("\nPress Enter to Return to Main Menu...")
