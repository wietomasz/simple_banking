
class Transaction:
    def __init__(self, type: str, clientID: int, transactionID: int, amount: float = 0) -> object:
        self.type = type
        self.clientID = clientID
        self.transactionID = transactionID
        self.amount = amount

    def __str__(self):
        return str(self.__dict__)

