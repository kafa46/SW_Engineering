'''연관(Association) 및 의존(Depencency) 관계의 차이점 설명합니다.
Author: Giseop Noh
License: MIT License
'''

class CellPhone:
    '''휴대폰 클래스'''

    def __init__(self, phone_number: str) -> None:
        self.phone_number: str = phone_number

    def send_text(self, number: str, msg: str):
        '''저정한 전화번호(number)로 문자메시지(msg) 전송'''
        print(f'{number}님께 문자 전송: {msg}')

    def voice_call(self, number: str):
        '''지정한 전화번호(number)로 음성통화'''
        print(f'{number}님과 음성통화가 연결되었습니다.')


class PersonWithPhone():
    '''휴대폰을 소유한 사람'''

    def __init__(self, name:str, phone: CellPhone) -> None:
        self.name: str = name
        self.phone: CellPhone = phone

    def send_msg_using_phone(self, number: str, msg: str):
        '''자신이 소유한 휴대폰을 사용하여 문자 발송 '''
        self.phone.send_text(number, msg)


class PersonWithoutPhone():
    '''휴대폰이 없어서 빌려쓰는 사람'''
    def __init__(self, name:str) -> None:
        self.name: str = name
    
    def send_msg_using_phone(self, number: str, msg: str, phone: CellPhone):
        '''휴대폰을 빌려서 문자 발송 '''
        phone.send_text(number, msg)
    

if __name__=='__main__':
    phone = CellPhone('010-1234-5555')
    person_with_phone = PersonWithPhone('Hong Gil Dong', phone)
    person_with_phone.send_msg_using_phone('010-1234-9999', 'Hello world')

    phone = CellPhone('010-5555-6789')
    persson_without_phone = PersonWithoutPhone('Hong Gil Dong')
    persson_without_phone.send_msg_using_phone('010-1234-9999', 'Hello world', phone)