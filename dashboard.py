def show_dashboard(workbook):

    customers_sheet = workbook["customers"]
    products_sheet = workbook["products"]
    orders_sheet = workbook["orders"]

    # -------------------------
    # CUSTOMER SUMMARY
    # -------------------------

    total_customers = customers_sheet.max_row - 1

    # -------------------------
    # PRODUCT SUMMARY
    # -------------------------

    total_products = products_sheet.max_row - 1

    total_stock = 0
    low_stock = 0
    out_of_stock = 0

    for row in products_sheet.iter_rows(min_row=2, values_only=True):

        stock = row[4]

        if stock is not None:

            total_stock += stock

            if stock == 0:
                out_of_stock += 1

            elif stock <= 55:
                low_stock += 1

    # -------------------------
    # ORDER SUMMARY
    # -------------------------

    total_orders = orders_sheet.max_row - 1

    # -------------------------
    # DISPLAY DASHBOARD
    # -------------------------

    print()
    print("=" * 50)
    print("          SUPERMART DASHBOARD")
    print("=" * 50)

    print()

    print("CUSTOMER SUMMARY")
    print("-" * 30)
    print("Total Customers    :", total_customers)

    print()

    print("PRODUCT SUMMARY")
    print("-" * 30)
    print("Total Products     :", total_products)
    print("Total Stock        :", total_stock)
    print("Low Stock Products :", low_stock)
    print("Out Of Stock       :", out_of_stock)

    print()

    print("ORDER SUMMARY")
    print("-" * 30)
    print("Total Orders       :", total_orders)

    print()

    print("=" * 50)
    print("          END OF DASHBOARD")
    print("=" * 50)

    input("\nPress Enter to Return to Main Menu...")