class Menu:
    def __init__(self):
        self.items = {
            "Burger Steak": 100,
            "French Fries": 60,
            "Fried Chicken": 130,
            "Pancit": 90,
            "Clubhouse": 120,
            "Iced Tea": 45
        }

    def display(self):
        print("\n========== MENU ==========")
        for item, price in self.items.items():
            print(f"{item:<15} ₱{price:.2f}")
        print("===========================")

    def has_item(self, item_name):
        return item_name in self.items

    def get_price(self, item_name):
        return self.items[item_name]


class OrderItem:
    def __init__(self, item, quantity, price):
        self.item = item
        self.quantity = quantity
        self.price = price

    def get_total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, menu):
        self.menu = menu
        self.items = []

    def ask_to_order(self):
        while True:
            answer = input("\nDo you want to order? (yes/no): ").lower()

            if answer == "yes" or answer == "y":
                return True
            elif answer == "no" or answer == "n":
                return False
            else:
                print("Please enter yes or no.")

    def ask_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    return quantity
                else:
                    print("Quantity must be greater than 0.")

            except ValueError:
                print("Please enter a valid number.")

    def ask_another(self):
        while True:
            another = input(
                "\nDo you want to order another item? (yes/no): "
            ).lower()

            if another == "yes" or another == "y":
                return True
            elif another == "no" or another == "n":
                return False
            else:
                print("Please enter yes or no.")

    def take_orders(self):
        while True:
            item_name = input("\nEnter the menu item: ").title()

            if not self.menu.has_item(item_name):
                print("Sorry, that item is not on the menu.")
                continue

            quantity = self.ask_quantity()
            price = self.menu.get_price(item_name)

            self.items.append(OrderItem(item_name, quantity, price))

            if not self.ask_another():
                break

    def calculate_total(self):
        total = 0

        for order_item in self.items:
            total += order_item.get_total()

        return total


class Receipt:
    def __init__(self, order):
        self.order = order

    def print_receipt(self):
        print("\n\n========== RECEIPT ==========")
        print(f"{'Item':<15}{'Qty':<8}{'Price':<10}{'Total':<10}")
        print("-------------------------------------------")

        # For loop is used to print the order details
        for order_item in self.order.items:
            print(
                f"{order_item.item:<15}"
                f"{order_item.quantity:<8}"
                f"₱{order_item.price:<9.2f}"
                f"₱{order_item.get_total():<9.2f}"
            )

        print("-------------------------------------------")
        print(f"TOTAL ORDER: ₱{self.order.calculate_total():.2f}")
        print("==============================")
        print("Thank you for ordering!")