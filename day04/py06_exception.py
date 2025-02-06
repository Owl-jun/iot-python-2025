# py06_exception.py

# 예외처리
## 오류, Error, 실수, Fault
## 1. Error(문법적 오류 syntax error) // ex) 코딩하다가 빨간색 밑줄
## 2. Exception(실행중 발생 예외) // ex) 문법오류 수정 후 실행 도중 비정상 종료
## 파이썬은 Error도 Error , Exception도 Error
## 에디터 상에 오류표시가 나면 Error
## 실행 중에 발생하면 Exception

mul = lambda a,b : a*b
div = lambda a,b : a/b

while True :
    op = input('계산할 연산을 입력(*, /, q) : ')
    if op == 'q' : break

    while True :
        try :
            x , y = map(int,(input('계산할 숫자 두개 입력, (스페이스바로 분리) : ').split(' ')))
            break
        except ValueError :
            print("잘못된 입력입니다. 스페이스로 분리해주세요 ex) 3 7")
            continue

    if op == '*' : print(f'{x} * {y} = {mul(x,y)}'); break
    elif op == '/' : print(f'{x} / {y} = {div(x,y)}'); break
    else : print('입력이 잘못되었답니다. 나가려면 q 입력')
