
class User:

    transactions = []

    def __init__(self, userID: int, available: float, held: float, total: float, locked: bool, transactions = None):
        self.userID = userID
        self.available = available
        self.held = held
        self.total = total
        self.locked = locked
        self.transactions = transactions or []

    def __str__(self):
        return str(self.__dict__)

    #User bank operations

    def deposit(self, amount: float):
        if self.locked:
            print("Account locked, cant process transaction")
            return self
        self.available += amount
        self.total += amount

    def withdraw(self, amount: float):
        if self.locked:
            print("Account locked, cant process transaction")
            return self
        if (self.available < amount):
            print(f'Insufficient Funds: User Id: {self.userID}, available balance: {self.available}, '
                  f'amount to withdraw: {amount}')
            return self
        self.available -= amount
        self.total -= amount

    def dispute(self, amount: float):
        if self.locked:
            print("Account locked, cant process transaction")
            return self
        self.available -= amount
        self.held += amount

    def resolve(self, amount: float):
        if self.locked:
            print("Account locked, cant process transaction")
            return self
        self.held -= amount
        self.available += amount

    def chargeback(self, amount: float):
        if self.locked:
            print("Account locked, cant process transaction")
            return self
        self.total -= amount
        self.held -= amount
        self.locked = True