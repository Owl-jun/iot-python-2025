# py06.oop.py

# 객체지향 - Object
#   속성변수(멤버변수) = 값
#   
#   def 함수(self, 매개변수):
#       실행문
#       return ...
# 클래스는 명사(변수)와 동사(함수)의 집합



class person:
    def __init__(self,_name,_age):
        self.__name = _name
        self.__age = _age

    def get_age(self):
        return self.__age
    
    get_name = lambda self : self.__name

    def walk(self) :
        print("걷기를 시작합니다.")
    


jun = person("jun",31)
# jun.__age = 32 , __ == private , 접근불가
print(jun.get_age())
print(jun.get_name())
jun.walk()