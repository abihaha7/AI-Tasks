class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("❌ Insufficient balance!")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

# Example Usage
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  
