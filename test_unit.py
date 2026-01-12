import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility


# ---------- deposit ----------
def test_deposit_valid():
    assert deposit(1000, 500) == 1500


def test_deposit_boundary():
    with pytest.raises(ValueError):
        deposit(1000, 0)


def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, -100)


# ---------- withdraw ----------
def test_withdraw_valid():
    assert withdraw(1000, 400) == 600


def test_withdraw_boundary():
    with pytest.raises(ValueError):
        withdraw(1000, 0)


def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(500, 1000)


# ---------- calculate_interest ----------
def test_calculate_interest_valid():
    result = calculate_interest(1000, 10, 2)
    assert result == pytest.approx(1210)


def test_calculate_interest_negative_balance():
    with pytest.raises(ValueError):
        calculate_interest(-100, 10, 1)


def test_calculate_interest_negative_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 1)


# ---------- check_loan_eligibility ----------
def test_loan_eligible():
    assert check_loan_eligibility(6000, 750) is True


def test_loan_not_eligible():
    assert check_loan_eligibility(3000, 650) is False


def test_loan_negative_balance():
    with pytest.raises(ValueError):
        check_loan_eligibility(-500, 700)
