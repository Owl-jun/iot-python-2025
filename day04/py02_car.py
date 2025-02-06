# py02_car.py

# 객체지향 다시

import re
 
class Car:

    ## __new__, __init__ : 생성자
    ## Car() 호출하면 아래의 메서드가 실행
    ## __ <- private
    def __init__(self, _company = None, _name = None, _plateNumber = None) :
        self.__company = _company
        self.__name = _name
        self.__plateNumber = _plateNumber
        print('Car 클래스를 새로 생성!')

    def __str__(self) :
        return f'제 차는 {self.get_name()} 이고, 차 번호는 {self.get_plateNumber()} 입니다.'

    get_company = lambda self : self.__company
    get_name = lambda self : self.__name
    get_plateNumber = lambda self : self.__plateNumber

    def set_plateNumber(self,new_pN) : 
        # 차량번호 규칙 생성 숫자 2-3자리 + 한글1자 + 숫자 4자리
        p = re.compile('^\d{2,3}[가-힣]{1}\d{4}$') 
        if p.match(new_pN) :
            self.__plateNumber = new_pN
    def set_name(self,new_name) :
        if type(new_name) is str :
            self.__name = new_name
    def set_company(self,new_com) :
        if type(new_com) is str :
            self.__company = new_com

if __name__ == "__main__" :
    myCar = Car('Hyundai','santafe','27모9135')
    print(myCar.get_plateNumber())
    myCar.set_plateNumber("99노3030")
    print(myCar.get_plateNumber())
    myCar.set_plateNumber("99a3030")
    print(myCar.get_plateNumber())
    print(myCar)
    print(myCar.get_name())
    print(myCar.get_company())


class test :
    pass

    


