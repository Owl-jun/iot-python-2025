# py04_stringformat.py
# 문자열 포맷팅

loginTemp = "안녕하세요, %s 님!"
name = "성명건"
cash = 35000
print(loginTemp % (name))
print("반갑습니다. %s 님 오늘 총 결제 금액은 %d원 입니다." %(name,cash))

# name = input("로그인할 이름 입력 > ")
# print(loginTemp % (name))


## 구세대 문자열 포맷팅
intro = '나는 %s(이)고, %d살 입니다. 몸무게 %fkg 입니다'
name = "강석준"
age = 31
weight = 71.3
print(intro %(name,age,weight))

intro = '나는 %10s(이)고, %05d살 입니다. 몸무게 %10.1fkg 입니다'
print(intro %(name,age,weight))

## 중간세대 문자열 포맷팅
intro = '나는 {0:10s} 이고, {1}살 입니다. 몸무게는 {2}kg 입니다.'
print(intro.format(name,age,weight))

## 신세대 문자열 포맷팅
print(f"내이름은 {name:^10s}이고, 나이는 {age}이다.")