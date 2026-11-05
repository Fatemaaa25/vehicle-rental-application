import pytest
from rental_balance import check_rental_balance


@pytest.mark.parametrize(
    "balance, requested, expected",
    [
        (10, 1, True),    # one day
        (2, 5, False),    # multiple days
        (10, 0, False),   # zero
        (10, -1, False),  # invalid input
    ],
)
def test_rental_balance(balance, requested, expected):
    assert check_rental_balance(balance, requested) is expected