import datetime
from tabulate import tabulate

MENU = {
    "espresso": 3.50,
    "cappuccino": 5.50,
    "latte": 6.00,
    "iced-coffee": 6.00,
    "mocha": 5.00,
    "tea": 3.00,
}


def display_welcome_message():
    print("Welcome to the Cafe Order App!")


def display_menu():
    menu_data = [[item.capitalize(), f"${price:.2f}"]
                 for item, price in MENU.items()]
    print("\nMenu:")
    print(tabulate(menu_data, headers=["Item", "Price"], tablefmt="grid"))


def get_order():
    order = {}
    while True:
        item = input(
            "\nSelect an item from the menu (or type 'done' to finish): ").lower()
        if item == "done":
            break
        if item in MENU:
            if item in order:
                order[item] += 1
            else:
                order[item] = 1
        else:
            print("Invalid selection, please try again.")
    return order


def calculate_total(order):
    total = 0
    for item in order:
        total += MENU[item]
    return total


def display_order_summary(order, total):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    order_data = [[quantity, item.capitalize(), f"${MENU[item] * quantity:.2f}"]
                  for item, quantity in order.items()]

    print(f"\nOrder Summary ({current_time}):")
    print(tabulate(order_data, headers=[
          "Quantity", "Item", "Price"], tablefmt="grid"))
    print(f"\nTotal: ${total:.2f}")


def get_payment(total):
    while True:
        try:
            payment = float(input("\nEnter payment amount: $"))
            if payment >= total:
                return payment
            else:
                print("Insufficient payment, please try again.")
        except ValueError:
            print("Invalid input, please enter a valid number.")
