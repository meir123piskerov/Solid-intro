from classes.ocp_2.Payment import Payment


class CryptoPayment(Payment):
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print(f"CryptoPayment: {self.amount}")
