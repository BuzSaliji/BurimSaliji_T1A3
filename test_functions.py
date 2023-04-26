import pytest
from functions import calculate_total, get_payment


@pytest.mark.parametrize("order, expected_total", [
    ({"espresso": 2, "cappuccino": 1}, 2 * 3.50 + 1 * 5.50),
    ({"latte": 3, "tea": 1}, 3 * 6.00 + 1 * 3.00)
])
def test_calculate_total(order, expected_total):
    actual_total = calculate_total(order)
    assert actual_total == expected_total, f"Expected {expected_total}, but got {actual_total}"


@pytest.mark.parametrize("total, test_payment, expected_payment", [
    (10.00, 12.00, 12.00),
    (20.00, 20.00, 20.00)
])
def test_get_payment(total, test_payment, expected_payment):
    actual_payment = get_payment(
        total, validate=True, test_payment=test_payment)
    assert actual_payment == expected_payment, f"Expected {expected_payment}, but got {actual_payment}"
