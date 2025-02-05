# yield 연습 및 숙달

# 문제 1: 간단한 제너레이터 만들기
# 1부터 5까지의 숫자를 반환하는 제너레이터 함수를 작성하세요.

def make_gen() :
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

gen = make_gen() # 제네레이터 객체

# 문제 2: 제너레이터로 피보나치 수열 생성하기
# 피보나치 수열의 첫 N개의 숫자를 반환하는 제너레이터 함수를 작성하세요. N은 함수의 인자로 받습니다.

def fibo_gen(n) :
    a,b = 0,1
    for _ in range(n) :
        yield a
        a , b = b, a+b

fibo = fibo_gen(6)
for _ in fibo :
    print(_, end=' ')
print()

# 문제 3: 무한 제너레이터 만들기
# 무한히 증가하는 자연수를 반환하는 제너레이터 함수를 작성하세요. 이 제너레이터는 next()가 호출될 때마다 다음 자연수를 반환해야 합니다.

def infinite_num() :
    a = 1
    while 1 :
        yield a
        a = a+1

num = infinite_num()
for i in range(10) :
    next(num)
count = next(num)
print(count)

# 문제 4: 제너레이터로 리스트의 요소 필터링하기
# 주어진 리스트에서 짝수만 반환하는 제너레이터 함수를 작성하세요. 리스트는 함수의 인자로 받습니다.

def evenFilter(_list) :
    for i in _list :
        if i & 1 == 0 :
            yield i

testList = [1,4,5,2,3,11,14]
y = evenFilter(testList)
for i in y :
    print(i,end=' ')
print()

# 문제 5: 제너레이터로 파일 읽기
# 텍스트 파일을 한 줄씩 읽어 반환하는 제너레이터 함수를 작성하세요. 파일 이름은 함수의 인자로 받습니다. (파일이 존재한다고 가정합니다.)

def read_Data(file):
    for line in file:
        yield line

with open('./day03/test.txt', mode='r', encoding='utf-8') as f:
    y1 = read_Data(f)
    print(next(y1))
    print(next(y1))


# 문제 6: 제너레이터로 조합 생성하기
# 주어진 리스트의 모든 조합을 생성하는 제너레이터 함수를 작성하세요. 예를 들어, 리스트가 [1, 2]일 경우, (1,), (2,), (1, 2)와 같은 조합을 반환해야 합니다.

from itertools import combinations

def generate_combinations(lst):
    for r in range(1, len(lst) + 1):
        for combo in combinations(lst, r):
            yield combo

data = [1, 2]
for combo in generate_combinations(data):
    print(combo)


