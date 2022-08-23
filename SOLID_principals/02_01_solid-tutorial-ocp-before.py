#-*- coding: utf-8 -*-

'''
Related YouTube Tutorial: https://youtu.be/pTB30aXS77U
Original Source Code: https://github.com/ArjanCodes/betterpython/tree/main/9%20-%20solid
'''

# 기존 클래스
class Order:
    '''Order class'''
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        '''Add items into Order'''
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        '''Get total price'''
        total = 0
        for idx, _ in enumerate(self.prices):
            total += self.quantities[idx] * self.prices[idx]
        return total


class PaymentProcessor:
    '''주문 결재 처리기:
    Odder 클래스에서 책임(pay)을 분리하기 구현한 클래스
    '''

    def pay_debit(self, order, security_code):
        '''직불 카드 결재'''
        print("직불카드 결재를 시작합니다.")
        print(f"비밀번호 확인: {security_code}")
        print('결재가 완료되었습니다.')
        order.status = "paid"

    def pay_credit(self, order, security_code):
        '''신용 카드 결재'''
        print("신용카드 결재를 시작합니다.")
        print(f"비밀번호 확인: {security_code}")
        print('결재가 완료되었습니다.')
        order.status = "paid"


if __name__=='__main__':
    # Order 객체 생성 및 실행
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)
    print(f'결재 금액은 {order.total_price()} 입니다.')

    # PaymentProcess 객체 생성 및 실행
    processor = PaymentProcessor()
    processor.pay_debit(order, "0372846")
