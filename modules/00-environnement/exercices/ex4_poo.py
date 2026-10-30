"""Exercice 4 : programmation orientée objet (classe, héritage, méthodes spéciales).

Tests : uv run pytest modules/00-environnement/exercices/test_ex4_poo.py
"""


class BankAccount:
    """Un compte bancaire.

    account = BankAccount("Hadrien")        # solde initial : 0
    account = BankAccount("Hadrien", 100)   # ou un solde initial au choix
    account.deposit(50)                     # solde + 50
    account.withdraw(30)                    # solde - 30
    account.balance                         # le solde actuel
    repr(account)  ->  "BankAccount('Hadrien', 120)"

    - deposit et withdraw lèvent une ValueError si le montant est négatif ou nul.
    - withdraw lève une ValueError si le solde est insuffisant, et le solde ne bouge pas.
    """


class SavingsAccount(BankAccount):
    """Un compte épargne : un BankAccount qui a en plus un taux d'intérêt.

    savings = SavingsAccount("Hadrien", 1000, rate=0.02)
    savings.add_interest()   # solde : 1020
    savings.deposit(10)      # hérité de BankAccount, sans le réécrire
    repr(SavingsAccount("Hadrien", 500, rate=0.02))  ->  "SavingsAccount('Hadrien', 500)"
    """
