import datetime
import csv
from tabulate import tabulate
from termcolor import colored


MENU = {
    "espresso": 3.50,
    "cappuccino": 5.50,
    "latte": 6.00,
    "frappe": 6.00,
    "mocha": 5.00,
    "tea": 3.00,
}


def display_welcome_message():
    print(colored("Welcome to the Cafe Order App!", "yellow"))


def display_menu():
    menu_data = [[colored(item.capitalize(), "yellow"), colored(f"${price:.2f}", "yellow")]
                 for item, price in MENU.items()]
    headers = [colored("Item", "yellow"), colored("Price", "yellow")]
    table = tabulate(menu_data, headers=headers, tablefmt="grid")
    table = table.replace('+', colored('+', 'blue'))
    table = table.replace('-', colored('-', 'blue'))
    table = table.replace('|', colored('|', 'blue'))
    table = table.replace('=', colored('=', 'blue'))

    print(colored("\nMenu:", "yellow"))
    print(table)


def get_order():
    order = {}
    while True:
        item = input(colored(
            "\nSelect an item from the menu (or type 'done' to finish): ", "yellow")).lower()
        if item == "done":
            break
        if item in MENU:
            try:
                quantity = int(
                    input(colored(f"How many {item.capitalize()} do you want to add? ", "yellow")))
                if quantity <= 0:
                    print("Please enter a valid quantity.")
                    continue
                if item in order:
                    order[item] += quantity
                else:
                    order[item] = quantity
            except ValueError:
                print(colored("Invalid input. Please enter a valid number.", "red"))
        else:
            print(colored("Invalid selection, please try again.", "red"))
    return order


def calculate_total(order):
    total = 0
    for item, quantity in order.items():
        total += MENU[item] * quantity
    return total


def display_order_summary(order, total):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    order_data = [[colored(quantity, "yellow"), colored(item.capitalize(), "yellow"), colored(f"${MENU[item] * quantity:.2f}", "yellow")]
                  for item, quantity in order.items()]

    print(colored(f"\nOrder Summary ({current_time}):", "yellow"))
    order_headers = [colored("Quantity", "yellow"), colored(
        "Item", "yellow"), colored("Price", "yellow")]
    order_table = tabulate(order_data, headers=order_headers, tablefmt="grid")
    order_table = order_table.replace('+', colored('+', 'blue'))
    order_table = order_table.replace('-', colored('-', 'blue'))
    order_table = order_table.replace('|', colored('|', 'blue'))
    order_table = order_table.replace('=', colored('=', 'blue'))
    print(order_table)
    print(colored(f"\nTotal: ${total:.2f}", "yellow"))


def get_payment(total, validate=False, test_payment=None):
    while True:
        if validate:
            payment = test_payment
        else:
            try:
                payment = float(
                    input(colored("\nEnter payment amount: $", "yellow")))
            except ValueError:
                print(colored("Invalid input, please enter a valid number.", "red"))
                continue

        if payment >= total:
            return payment
        else:
            print(colored("Insufficient payment, please try again.", "red"))
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
