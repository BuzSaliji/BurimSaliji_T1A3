from functions import (display_welcome_message,
                       display_menu, get_order, calculate_total, get_payment)


def main():
    display_welcome_message()
    display_menu()
    order = get_order()
    total = calculate_total(order)
    payment = get_payment(total)
    change = payment - total
    print(f"\nTotal: ${total:.2f}")


if __name__ == "__main__":
    main()
