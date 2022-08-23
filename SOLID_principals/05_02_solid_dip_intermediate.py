'''의존관계 역전 원칙을 설명합니다.
    Topic: 의존관계 역전 원칙: DIP (Dependency Inversion Principal)
    Reference: https://github.com/ArjanCodes/betterpython/blob/main/2%20-%20dependency%20inversion/dependency-inversion-before.py
    Author: Gisoep Noh
    License: MIT License
'''

class Light:
    '''전구 클래스'''    
    
    def turn_on(self,):
        print('전구: 전원이 켜졌습니다.')
    
    def turn_off(self,):
        print('전구: 전원이 꺼졌습니다.')


class Fan:
    '''선풍기 클래스'''
    
    def turn_on(self,):
        print('선풍기: 선풍기가 돌아갑니다.')
    
    def turn_off(self,):
        print('선풍기: 선풍기가 멈춥니다.')


class Switch:
    '''스위치 클래스'''
    
    def __init__(self, status: bool = False) -> None:
        self.switch_on = status
    
    def push(self, obj: object):
        '''전구 on/off를 제어하는 메서드'''
        if self.switch_on:
            obj.turn_off()
            self.switch_on = False
        else:
            obj.turn_on()
            self.switch_on = True


if __name__=='__main__': 
    light = Light() # 전구 객체 생성
    fan = Fan() # 선평기 객체 생성
    switch = Switch(status=False) # 스위치 객체 생성
    
    # 전구 제어
    switch.push(light) # 스위치 1번 누름: 전구 off -> on
    switch.push(light) # 스위치 1번 누름: 전구 on -> off

    # 선풍기 제어
    switch.push(fan) # 스위치 1번 누름: 선풍기 off -> on
    switch.push(fan) # 스위치 1번 누름: 선풍기 on -> off


