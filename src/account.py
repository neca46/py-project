class Account:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.balance = 0

    def get_account_info(self):
        print(f"Name of cusomer is {self.name}")
        print(f"Account balance is {self.balance}")

    def get_balance(self):
        return self.balance

    def add_balance(self, amount):
        if amount <= 0:
            print("Amount must be positive number")
            return None

        self.balance += amount
        return self.balance
