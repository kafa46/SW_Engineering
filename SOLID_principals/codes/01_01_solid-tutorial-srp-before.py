'''
Related YouTube Tutorial: https://youtu.be/pTB30aXS77U
Original Source Code: https://github.com/ArjanCodes/betterpython/tree/main/9%20-%20solid
'''

# 기존 클래스
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
    
    # Order와 관련 없는 책임
    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("직불카드 결재를 시작합니다.")
            print(f"비밀번호 확인: {security_code}")
            print('결재가 완료되었습니다.')
            self.status = "paid"
        elif payment_type == "credit":
            print("신용카드 결재를 시작합니다.")
            print(f"비밀번호 확인: {security_code}")
            print('결재가 완료되었습니다.')
            self.status = "paid"
        else:
            raise Exception(f"적용할 수 없는 결재 방법입니다: {payment_type}")


if __name__=='__main__':
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    print(f'결재 금액은 {order.total_price()} 입니다.')
    order.pay("debit", "0372846")