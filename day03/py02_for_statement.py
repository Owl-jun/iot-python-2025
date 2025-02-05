# py02_for_statement.py

# for문 : 프로그래밍의 꽃
# 반복을 처리할 때 사용
# for 변수 in 반복할값 :
#   명령문

n = int(input('최대 별 개수 : '))
for i in range(1,n+1) :
    print('*' * i)

# range() 범위를 생성하는 클래스
# print(range(8)) : return range(0,8)

for i in range(8,0,-1) :
    print(i)



# 구구단
# 2단부터

for i in range(2,10) :
    print(f"{i}단 시작")
    for j in range(1,10) :
        print(f'{i} x {j} = {i*j:2d}' , end=" ")
    print()


## 반복문을 빠져나오고 싶을 때 : break
## 반복문에서 특정 조건을 지나칠 때 : continue
