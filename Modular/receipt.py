def print_receipt(orders, total):
    print("\n\n========== RECEIPT ==========")
    print(f"{'Item':<15}{'Qty':<8}{'Price':<10}{'Total':<10}")
    print("-------------------------------------------")

    # For loop is used to print the order details
    for order in orders:
        print(
            f"{order['item']:<15}"
            f"{order['quantity']:<8}"
            f"₱{order['price']:<9.2f}"
            f"₱{order['total']:<9.2f}"
        )

    print("-------------------------------------------")
    print(f"TOTAL ORDER: ₱{total:.2f}")
    print("==============================")
    print("Thank you for ordering!")