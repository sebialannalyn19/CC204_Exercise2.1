from restaurant import Menu, Order, Receipt


def main():
    menu = Menu()
    menu.display()

    order = Order(menu)

    if order.ask_to_order():
        order.take_orders()

        receipt = Receipt(order)
        receipt.print_receipt()

    else:
        print("\nThank you! Have a nice day.")


main()