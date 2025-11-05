from classes.exe_3.Order import Order

class InvoicePrinter:
    @staticmethod
    def print_invoice(items : Order):
        for i in items.items:
            print(i)