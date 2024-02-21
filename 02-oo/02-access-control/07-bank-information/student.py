class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__acount_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__acount_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError(f"Cannot deposit zero or negative funds")
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(f"Cannot deposit zero or negative funds")
        if self.__balance - amount < 0:
            raise ValueError(f"Insufficient funds")
        self.__balance -= amount