# py03_module.py

# 모듈 - 레고
# import 모듈명
# from 모듈명 import 상세..

# 모듈화를 위해서는 예제 소스 (테스트 소스)를 주석처리해주자.
# import py02_car as c : py02_car 자체를 c 로 define 하겠다.
# from py02_car import Car : py02_car 안의 Car 클래스만! 가져오겠다.
# from py02_car import Car as c : py02_car 안의 Car 클래스를 c 라고 define 하겠다.
import py05_module as o
from py02_car import Car

a = Car('기아차','스팅어')
# b = test()
c = o.Sample()

print(c)
print(a)
