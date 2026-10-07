from customers import (view_customers, delete_customer , customer_search)

from products import(view_products, product_search, update_product_stock, restock_Product, low_stock_report, out_of_stock, delete_product)

from orders import(view_order, search_order, add_new_order, delete_order)

from utils import workbook

from dashboard import show_dashboard

while True:
    print("=" * 40)
    print("      SuperMart Management System")
    print("=" * 40)
    print("1. View Customers")
    print("2. Delete Customer")
    print("3. Search Customer")
    print("4. View Product")
    print("5. Search Product")
    print("6. Update Product Stock")
    print("7. Restock Product ")
    print("8. Low Stock Report ")
    print("9. Out Of Stock Report")
    print("10. Delete Product ")
    print("11. View Order")
    print("12. Search Order")
    print("13. Add New Order")
    print("14. Delete Order")
    print("15. Show Dashboard")
    print("0. Exit")
    choice = input("Enter Your Choice:- ")
   
    if choice == "1" :
        view_customers()
    elif choice == "2" :
        delete_customer()
    elif choice == "3" :
        customer_search()
    elif choice == "4" :
        view_products()
    elif choice == "5":
            product_search()
    elif choice == "6":
        update_product_stock()
    elif choice == "7":
        restock_Product()
    elif choice == "8":
        low_stock_report()
    elif choice == "9":
        out_of_stock()
    elif choice == "10":
        delete_product()
    elif choice == "11":
        view_order()
    elif choice =="12":
        search_order()
    elif choice == "13":
        add_new_order()
    elif choice == "14":
        delete_order()
    elif choice == "15":
        show_dashboard(workbook)
    elif choice =="0":
        print("Thanks for using SuperMart")
        break
    else :
        print("Invalid Choice")
    print()