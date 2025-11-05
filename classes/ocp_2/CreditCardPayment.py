from classes.ocp_2.Payment import Payment

class CreditCardPayment(Payment):
    def __init__(self, amount):
        self.amount = amount
    def pay(self):
        print(f'  CreditCardPayment: {self.amount}')

