# py01_list_op.py

# 리스트 연산
# 리스트가 for, while 반복문에서 가장 많이 활용되는 데이터 구조

# iterable -> 반복 할 수 있는 요소 인지
lst1 = [1,2,3]
lst2 = [4,5,6]
print(list(map(lambda x,y : x + y,lst1,lst2)))

arr = [1,2,3,4,5,1]

arr[2] = 9
print(len(arr))
del(arr[2]) ## 완전삭제 , 지우고 <- 땡겨
print(arr)

arr.append(3) ## push_back
arr.insert(2,3) ## insert 자리채우고 -> 땡겨
print(arr)

## 리스트 합칠 때
lst1.extend(lst2)
print(lst1)

## 리스트 정렬
sortList = [3,6,1,2,7,4,9]
sortList.sort(reverse=True)
print(sortList)

## 요소의 위치파악
print(arr.index(5)) ## 범위 초과 시 오류발생
print(arr.count(1)) ## 같은 요소 몇개?

## 요소 꺼내기
temp = arr.pop()
print(arr)
print(temp)

## 리스트 컴프리핸션
print(f'{sum([i for i in range(1,1001) if i & 1])} 입니다.')