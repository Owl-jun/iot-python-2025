# py05_operator.py
# 연산자

# 사칙연산 + - * /
a, b = 15, 14
print(a,b)

# Shift + Del 는 한줄 삭제 (매우 효율적)
print(a + b)
print(a - b)
print(a * b)

print(a / b) # 단순 나누기 -> float 
print(a % b) # 나머지 -> int
print(a // b) # 몫 -> int

# 거듭제곱(Power)
print(a ** 2)

# 연산자 우선순위
## 계산식이 복잡해서 연산자 우선순위를 잘 모르겠으면 () 사용.
print((3 + 4) * 7) # 49
print(3 + 4 * 7) # 31


## 리스트 연산
## index = list len - 1
listA = [1,2,3,4,5,6]
listB = list([1,2,3,4,5,6])

print(listA + listB)
print(len(listA))

for i in range(len(listA)) :
    print(listA[i] + listB[i])


## 문자열 연산 :  +,* 만 존재
greeting = "Hello World"
surprise = "!"

print(greeting + surprise) # string concatenate
print(f"{greeting}{surprise}")
print(greeting[0:5] + surprise)
print(greeting * 5) # 해당 문자열을 n회 반복

## 문자열(Charactor Array) == List but, 인덱스로 접근해서 값 변경 불가
print(greeting[1]) # 리스트 연산

## 슬라이싱 [start:end] : end -1 값 까지만 추출 
listSample = ['2','0','2','5','-','0','2','-','0','4']
current = '2025-02-04'
for i in listSample:
    print(i, end='')
print()
print(listSample[0:4])
print(current[0:4])
print(current[-2:])

# 준비 끝

# 인덱싱, 인덱스에 있는 값을 가져오기
print(listSample[9])
print(current[-1])


# 2025-02-04
year = current[:4]
month = current[5:7]
day = current[8:]

print(f"{year}{month}{day}")

## 문자열 연산 중 함수를 사용
fullName = "Seokjun Kang"

# split
print(fullName.split())
print(fullName.split("K"))
names = fullName.split() # split 시 리스트 값이 리턴됨
print(names)

# replace
print(fullName.replace('Kang','David'))

# 공백제거 (strip) , lstrip 좌측 제거 // rstrip 우측 제거
origin = '              ge qo   '
print(origin.strip())
print(f"//{origin.strip()}//")
print(f"//{origin.lstrip()}//")
print(f"//{origin.rstrip()}//")

# find("str",begin,end) -> index값 리턴, 못찾으면 -1 리턴
print(fullName.find("n",fullName.find("n")+1,))

# count 문자열 값이 몇번 나오는가
print(fullName.count("n"))

# index 인덱스 값 돌려줌, 근데 없으면 에러 (예외처리 해줘야 한다.)
print(fullName.index('n'))

# 대소문자 변환
print(fullName.upper())
print(fullName.lower())

