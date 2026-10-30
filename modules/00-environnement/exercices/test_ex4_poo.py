import pytest

from ex4_poo import BankAccount, SavingsAccount


def test_default_balance_is_zero():
    assert BankAccount("Hadrien").balance == 0


def test_deposit_and_withdraw():
    account = BankAccount("Hadrien", 100)
    account.deposit(50)
    account.withdraw(30)
    assert account.balance == 120


def test_invalid_amounts():
    account = BankAccount("Hadrien", 100)
    with pytest.raises(ValueError):
        account.deposit(0)
    with pytest.raises(ValueError):
        account.withdraw(-5)


def test_withdraw_too_much():
    account = BankAccount("Hadrien", 100)
    with pytest.raises(ValueError):
        account.withdraw(500)
    assert account.balance == 100


def test_repr():
    assert repr(BankAccount("Hadrien", 120)) == "BankAccount('Hadrien', 120)"


def test_savings_interest():
    savings = SavingsAccount("Hadrien", 1000, rate=0.02)
    savings.add_interest()
    assert savings.balance == pytest.approx(1020)


def test_savings_inherits_deposit():
    savings = SavingsAccount("Hadrien", 1000, rate=0.02)
    savings.deposit(10)
    assert savings.balance == 1010
    # deposit doit venir de BankAccount, pas être réécrite dans SavingsAccount
    assert "deposit" not in SavingsAccount.__dict__


def test_savings_repr():
    assert repr(SavingsAccount("Hadrien", 500, rate=0.02)) == "SavingsAccount('Hadrien', 500)"
