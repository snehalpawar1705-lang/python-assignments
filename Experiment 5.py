class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn Rs {amount}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current Balance: Rs {self.balance}")


account = BankAccount(101, 5000)
account.deposit(2000)
account.withdraw(1500)
account.check_balance()
  