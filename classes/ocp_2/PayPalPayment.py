from classes.ocp_2.Payment import Payment


class PayPalPayment(Payment):
    def __init__(self,amount):
        self.amount = amount
    def pay(self):
        print(f'PayPalPayment: {self.amount}')

