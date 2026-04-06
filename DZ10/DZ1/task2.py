class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.__account_number = account_number  # private — not accessible from outside
        self.__balance = balance                # private — only via deposit/withdraw
        self.__account_holder = account_holder  # private storage, exposed via property

    @property
    def account_holder(self):
        return self.__account_holder

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance