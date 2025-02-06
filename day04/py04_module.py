# py04_module.py

# 수학모듈 : 수학함수들이 모여있는 파이썬 모듈

import math
import random

print(math.pi) # int
print(math.pow(2,3)) # float
print(math.sqrt(16))
print(math.log10(100))



# 초간단 로또
# weight : 가중치
result = []
numbers = list(range(1,46))
result.append(random.sample(numbers,6))
print(result)