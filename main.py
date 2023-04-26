from functions import (display_welcome_message,
                       display_menu, get_order, calculate_total, get_payment, display_order_summary, summary_file)


def main():
    display_welcome_message()
    display_menu()
    order = get_order()
    total = calculate_total(order)
    display_order_summary(order, total)
    summary_file(order_data, total, current_time)
    payment = get_payment(total)
    change = payment - total
    print(f"\nPayment accepted. Change: ${change:.2f}")
    print("Thank you for your order!")


if __name__ == "__main__":
    main()
