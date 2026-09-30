from display import display_menu
from orders import ask_to_order, get_orders
from total import calculate_total
from receipt import print_receipt


def main():
    display_menu()

    if ask_to_order():
        orders = get_orders()

        total = calculate_total(orders)

        print_receipt(orders, total)

    else:
        print("\nThank you! Have a nice day.")


main()