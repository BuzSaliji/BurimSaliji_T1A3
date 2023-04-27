import datetime
import csv
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
            try:
                quantity = int(
                    input(f"How many {item.capitalize()} do you want to add? "))
                if quantity <= 0:
                    print("Please enter a valid quantity.")
                    continue
                if item in order:
                    order[item] += quantity
                else:
                    order[item] = quantity
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid selection, please try again.")
    return order


def calculate_total(order):
    total = 0
    for item, quantity in order.items():
        total += MENU[item] * quantity
    return total


def display_order_summary(order, total):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    order_data = [[quantity, item.capitalize(), f"${MENU[item] * quantity:.2f}"]
                  for item, quantity in order.items()]

    print(f"\nOrder Summary ({current_time}):")
    print(tabulate(order_data, headers=[
          "Quantity", "Item", "Price"], tablefmt="grid"))
    print(f"\nTotal: ${total:.2f}")


def get_payment(total, validate=False, test_payment=None):
    while True:
        if validate:
            payment = test_payment
        else:
            try:
                payment = float(input("\nEnter payment amount: $"))
            except ValueError:
                print("Invalid input, please enter a valid number.")
                continue

        if payment >= total:
            return payment
        else:
            print("Insufficient payment, please try again.")
            if validate:
                break


def receipt(order, total, current_time):
    filename = f"receipt_{current_time.replace(':', '-')}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([f"Receipt ({current_time}):"])
        for item, quantity in order.items():
            price = f"${MENU[item] * quantity:.2f}"
            writer.writerow([f"{quantity} x {item.capitalize()}: {price}"])
        writer.writerow([f"Total: {total:.2f}"])
