from functions import (display_welcome_message,
                       display_menu, get_order, calculate_total)


def main():
    display_welcome_message()
    display_menu()
    order = get_order()
    total = calculate_total(order)
    print(f"\nTotal: ${total:.2f}")


if __name__ == "__main__":
    main()
