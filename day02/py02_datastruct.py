# py02_datastruct.py
# 복합자료형
# 자료구조 및 알고리즘

# 리스트 이전 ,, 귀찮음
a = 1
b = 2
c = 3
d = 4
e = 5

sum = a+b+c+d+e
print(sum)

## 리스트[] 사용 - 다른언어에선 리스트와 배열은 다른 것
f = [1,2,3,4,5]
print(f)
print(type(f))

f = ["life","is","true",0,None]
print(f)
print(f[0])

# 리스트의 한 요소에도 값을 집어넣을 수 있음
f[3] = 100
print(f)

## 튜플()
# 리스트와 거의 흡사. 값을 변경할 수 없음
t = (1,2,3,4)
print(t)
# t[0] = 5

## 딕셔너리 {key : value} 의 집합
spiderman = { "name" : "peter parker" , "age" : 20 , "weapon" : "web shooter" }
print(spiderman.keys())
print(spiderman.values())
print(spiderman)

print(spiderman["weapon"])
spiderman["name"] = 21
print(spiderman["age"])

## set (집합) (),[],{} 모두 사용가능 , 중복된 값을 허용하지 않음, 순서 없음 (빠른 처리를 위해 비순차적 알고리즘을 사용?)
s = set([1,2,3,4,4,4])
print(s)

s = set("Hello World")
print(s)

## 변수명 지정 방식
## 의미있는 단어들의 조합으로 만들 것
## ex)
phoneNumber = "999-99999-999"
salaryBankAccount = "866-12-334466"

samsung = ''
samsung1 = ''
## 1samsung = '' 숫자로 시작 불가
_samsung = ''
samsung_ = ''
## samsung! = '' _ 이외의 특수문자 사용불가
## samsung* = ''
## sam-sung = ''
## sam sung = '' 공백 불가