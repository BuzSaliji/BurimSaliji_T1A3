import pytest
from functions import calculate_total

# Test 1: Calculate Total


@pytest.mark.parametrize("order, expected_total", [
    ({"espresso": 2, "cappuccino": 1}, 2 * 3.50 + 1 * 5.50),
    ({"latte": 3, "tea": 1}, 3 * 6.00 + 1 * 3.00)
])
def test_calculate_total(order, expected_total):
    actual_total = calculate_total(order)
    assert actual_total == expected_total, f"Expected {expected_total}, but got {actual_total}"
