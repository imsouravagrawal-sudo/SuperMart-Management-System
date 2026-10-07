from utils import Customers_sheet,workbook
from logger import log_activity

def view_customers():
    print("CustomerID\tName\t\tCity")
    print("-" * 37)

    for row in Customers_sheet.iter_rows(min_row=2, values_only=True):
        print(row[0], "\t", row[1], "\t", row[2])

def delete_customer():
    customer_id = input("Enter Customer ID to Delete:- ")

    for row in Customers_sheet.iter_rows(min_row=2):
        if row[0].value == customer_id:
            Customers_sheet.delete_rows(row[0].row)

            workbook.save("data/SuperMart_Raw_Data.xlsx")
            log_activity("Customer deleted successfully.")
            print("\nCustomerr Deleted Successfully!")
            input("\nPress Enter to Return to Main Menu...")
            return
    else:     
        print("\nCustomer Not Found!")
        log_activity("Customer not found.")
        input("\nPress Enter to Return to Main Menu...")

def customer_search():
    customerid = input("Enter CustomeID:- ")

    for row in Customers_sheet.iter_rows(min_row=2, value_only=True):
        if row[0] == customerid:
            print("Customer Found!")
            print("CustomerId:-", row[0])
            print("Name:- ", row[1])
            print("City:-", row[2])
            break
    else :
        print("Customer Not Found!")
        log_activity("Customer not found.")