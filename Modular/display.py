from menu import menu


def display_menu():
    print("\n========== MENU ==========")
    for item, price in menu.items():
        print(f"{item:<15} ₱{price:.2f}")
    print("===========================")