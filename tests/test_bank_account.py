import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)

@pytest.fixture
def other_account():
    return BankAccount(100)


def test_invalid_initial_balance():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount(-1)

def test_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150

def test_invalid_deposit(start_account):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        start_account.deposit(-100)

def test_withdraw(start_account):
    start_account.withdraw(50)
    assert start_account.balance == 50

def test_invalid_withdraw(start_account):
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        start_account.withdraw(-100)

def test_insufficient_fund(start_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        start_account.withdraw(110)

def test_transfer_to(start_account, other_account):
    start_account.transfer_to(other_account, 50)
    assert start_account.balance == 50 and other_account.balance == 150

def test_invalid_target(start_account):
    other_account = None
    with pytest.raises(ValueError, match="Target must be a BankAccount"):
        start_account.transfer_to(other_account, 0)