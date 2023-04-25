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


def main():
    display_welcome_message()


if __name__ == "__main__":
    main()
