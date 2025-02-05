# py05_function.py

# 함수, Function, Method, Procedure...
# 인자, 파라미터, 매개변수 , argument ...
# def 함수명(인자, ...) :

# 제곱해서 돌려주는 함수
my_pow = lambda intList : [i**2 for i in intList]
print(my_pow([1,2,3,4]))
        
def say_hi() :
    return "hihihihihihihihi:)"

print(f'인사하기: {say_hi()}')


get_age = lambda x : 2025-x
print(get_age(1995))
