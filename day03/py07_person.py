# py07_person.py


class Person :
    def __init__(self,_name=None,_age=None,_weight=None,_gender=None):
        # 멤바 변수
        self.__name = _name
        self.__age = _age
        self.__weight = _weight
        self.__gender = _gender

    def __str__(self) : ## 객체 주소가아닌 보내주고 싶은 내용 보내주기
        return f"name : {self.__name} \t\nage : {self.__age} \t\nweight : {self.__weight} \t\ngender : {self.__gender}"
    
    # 멤바 함수 (메서드)
    get_name    =   lambda self : self.__name
    get_age     =   lambda self : self.__age
    get_weight  =   lambda self : self.__weight
    get_gender  =   lambda self : self.__gender
    def set_name(self,_name): self.__name = _name
    def set_age(self,_age): self.__age = _age
    def set_weight(self,_weight): self.__weight = _weight
    def set_gender(self,_gender): self.__gender = _gender
    def get_up(self): print(f'{self.__name}이(가) 일어납니다.')


man = Person()
man.set_age(35)
print(man.get_age())
jun = Person('jun',31,72,'male')
jun.get_up()
print(jun.get_name())
print(jun.get_age())
print(jun.get_weight())
print(jun.get_gender())
print(jun)