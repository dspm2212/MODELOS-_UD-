class PaymentMethod:
    def calculate_total(self, base_price):
        raise NotImplementedError("Subclass must implement abstract method")

# Pago de contado
class FullPayment(PaymentMethod):
    def calculate_total(self, base_price):
        return base_price

# Pago financiado
class FinancingPayment(PaymentMethod):
    def __init__(self, installments, interest_rate):
        self.installments = installments
        self.interest_rate = interest_rate

    def calculate_total(self, base_price):
        return base_price + base_price * (self.interest_rate / 100)