# 리스트 컴프리핸스 연습
# 짝수 필터링: 1부터 100까지의 숫자 중 짝수만 포함하는 리스트를 생성하세요.
def make_gen(lst) :
    for i in lst :
        yield i
gen = make_gen([i for i in range(1,101) if i & 1 == 0])
print(next(gen))
print(next(gen))


# 문자열 길이: 주어진 문자열 리스트에서 각 문자열의 길이를 포함하는 리스트를 만드세요.

_list = ["cheat","power","over","whelming"]
result = [len(i) for i in _list]
print(result)

# 제곱 계산: 1부터 10까지의 숫자에 대해 제곱을 계산하여 리스트로 만드세요.

powList = [i**2 for i in range(11) if i >= 1]
print(powList)

# 대문자 변환: 주어진 문자열 리스트에서 모든 문자열을 대문자로 변환한 리스트를 생성하세요.

_list2 = ["kang","seok","jun","fighting"]
upperList = [i.upper() for i in _list2]
print(upperList)

# 특정 문자 포함: 주어진 문자열 리스트에서 특정 문자를 포함하는 문자열만 필터링하여 새로운 리스트를 만드세요.

import re
p = re.compile(r'ha')
_list3 = ["have","happy","bye","good","soha","yiming"]
result2 = [i for i in _list3 if re.search(p,i)]
print(result2)

# 피보나치 수열: 피보나치 수열의 처음 10개 숫자를 포함하는 리스트를 생성하세요.

fibonacci_list = [0, 1]
[fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2]) for i in range(2, 10)]
print(fibonacci_list)

# 중복 제거: 주어진 리스트에서 중복된 요소를 제거하고, 고유한 요소만 포함하는 리스트를 만드세요.

_list4 = ["ab","ab","ac","d","d","q"]
result_list = []
[result_list.append(i) for i in _list4 if i not in result_list]
print(result_list)


print(len(_list4))