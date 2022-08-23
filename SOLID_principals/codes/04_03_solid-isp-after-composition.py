from abc import ABC, abstractmethod

class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class SMSAuth:
    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f'Verifying code: {code}')
        self.authorized = True
    
    def is_authorized(self,):
        return self.authorized


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: SMSAuth):
        self.authorizer = authorizer
        self.security_code = security_code
        
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: SMSAuth):
        self.authorizer = authorizer
        self.email_address = email_address

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"

if __name__=='__main__':
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    print(order.total_price())

    # Debit payment
    processor_debit = DebitPaymentProcessor('1234', SMSAuth())
    processor_debit.authorizer.verify_code('1234')
    processor_debit.pay(order)

    # Credit payment
    processor_credit = CreditPaymentProcessor('5678')
    processor_credit.pay(order)

    # Paypal payment
    processor_paypal = PaypalPaymentProcessor('abc@company.com', SMSAuth())
    processor_paypal.authorizer.verify_code('abc@company.com')
    processor_paypal.pay(order)