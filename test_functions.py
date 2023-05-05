import pytest
from functions import calculate_total, get_payment


# 1. Test: test_calculate_total
#    - Feature: Calculate the total cost of an order
#    - Description: This test checks if the calculate_total function correctly calculates the total cost of an order based on the items and their quantities.
#    - Test cases:
#      1. Input: {"espresso": 2, "cappuccino": 1}, Expected result: 2 * 3.50 + 1 * 5.50
#      2. Input: {"latte": 3, "tea": 1}, Expected result: 3 * 6.00 + 1 * 3.00

@pytest.mark.parametrize("order, expected_total", [
    ({"espresso": 2, "cappuccino": 1}, 2 * 3.50 + 1 * 5.50),
    ({"latte": 3, "tea": 1}, 3 * 6.00 + 1 * 3.00)
])
def test_calculate_total(order, expected_total):
    actual_total = calculate_total(order)
    assert actual_total == expected_total, f"Expected {expected_total}, but got {actual_total}"


# 2. Test: test_get_payment
#    - Feature: Validate the payment amount provided by the user
#    - Description: This test checks if the get_payment function correctly validates the payment amount and ensures it is sufficient to cover the total cost.
#    - Test cases:
#      1. Input: total = 10.00, test_payment = 12.00, Expected result: 12.00
#      2. Input: total = 20.00, test_payment = 20.00, Expected result: 20.00

@pytest.mark.parametrize("total, test_payment, expected_payment", [
    (10.00, 12.00, 12.00),
    (20.00, 20.00, 20.00)
])
def test_get_payment(total, test_payment, expected_payment):
    actual_payment = get_payment(
        total, validate=True, test_payment=test_payment)
    assert actual_payment == expected_payment, f"Expected {expected_payment}, but got {actual_payment}"
