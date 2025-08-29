# Thank you ChatGPT for this wonderful code

class BankAccount:
    def __init__(self, owner, balance=0.0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.owner = owner
        self.balance = float(balance)
        self.transactions = []  # keeps track of deposits/withdrawals

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self.transactions.append(("deposit", amount))
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(("withdraw", amount))
        return self.balance

    def get_balance(self):
        return self.balance

    def transfer_to(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise ValueError("Transfer target must be a BankAccount")
        self.withdraw(amount)
        other_account.deposit(amount)
        return self.balance, other_account.balance

    def last_transaction(self):
        if not self.transactions:
            return None
        return self.transactions[-1]

    def clear_transactions(self):
        self.transactions = []

