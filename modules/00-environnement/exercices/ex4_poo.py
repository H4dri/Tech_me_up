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
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0 :
            raise ValueError("Amount must be positive")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= 0 :
            raise ValueError("Amount must be positive")
        if amount > self.balance :
            raise ValueError("Insufficient funds")
        self.balance -= amount
    
    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.balance})"
    
    def __str__(self):
        return f"BankAccount owned by {self.owner} with balance {self.balance}"
    


class SavingsAccount(BankAccount):
    """Un compte épargne : un BankAccount qui a en plus un taux d'intérêt.

    savings = SavingsAccount("Hadrien", 1000, rate=0.02)
    savings.add_interest()   # solde : 1020
    savings.deposit(10)      # hérité de BankAccount, sans le réécrire
    repr(SavingsAccount("Hadrien", 500, rate=0.02))  ->  "SavingsAccount('Hadrien', 500)"
    """
    def __init__(self, owner, balance=0, rate=0.01):
        super().__init__(owner, balance)
        self.rate = rate
    
    def add_interest(self):
        self.balance += self.balance * self.rate
    
    def __repr__(self):
        return f"SavingsAccount('{self.owner}', {self.balance})"
    
    def __str__(self):
        return f"SavingsAccount owned by {self.owner} with balance {self.balance} and interest rate {self.rate}"
    