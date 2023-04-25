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
    for item, price in MENU.items():
        print(f"{item.capitalize()}: ${price:.2f}")


def get_order():
    order = {}
    while True:
        item = input(
            "\nSelect an item from the menu (or type 'done' to finish): ").lower()
        if item == "done":
            break
        if item in MENU:
            order[item] = 1
    return order


def calculate_total(order):
    total = 0
    for item in order:
        total += MENU[item]
    return total


def main():
    display_welcome_message()
    display_menu()
    order = get_order()


if __name__ == "__main__":
    main()
