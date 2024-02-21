
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Money(
            self.amount + other.amount,
            self.currency
            )
        raise RuntimeError(f"Mismatched currencies!")
    
    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(
            self.amount - other.amount,
            self.currency
            )
        raise RuntimeError(f"Mismatched currencies!")
    
    def __mul__(self, number):
        return Money(
        self.amount * number,
        self.currency
        )