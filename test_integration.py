import pytest
from bank_app import transfer, calculate_interest


def test_transfer_success():
    from_balance, to_balance = transfer(2000, 1000, 500)
    assert from_balance == 1500
    assert to_balance == 1500


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(300, 1000, 500)


def test_transfer_then_interest():
    from_balance, to_balance = transfer(5000, 2000, 1000)
    updated_balance = calculate_interest(to_balance, 5, 1)
    assert updated_balance == pytest.approx(3150)
