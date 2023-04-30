import datetime
from termcolor import colored
from functions import (display_welcome_message,
                       display_menu, get_order, calculate_total, get_payment, display_order_summary, receipt, MENU)


def main():
    display_welcome_message()
    display_menu()
    order = get_order()
    total = calculate_total(order)
    display_order_summary(order, total)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receipt(order, total, current_time)
    payment = get_payment(total)
    change = payment - total
    print(colored(f"\nPayment accepted. Change: ${change:.2f}", "green"))
    print(colored("Thank you for your order!", "green"))


if __name__ == "__main__":
    main()
