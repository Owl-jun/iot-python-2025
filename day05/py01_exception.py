# py01_exception.py

# 예외처리
## 오류, Error, 실수, Fault
## 1. Error(문법적 오류 syntax error) // ex) 코딩하다가 빨간색 밑줄
## 2. Exception(실행중 발생 예외) // ex) 문법오류 수정 후 실행 도중 비정상 종료
## 파이썬은 Error도 Error , Exception도 Error
## 에디터 상에 오류표시가 나면 Error
## 실행 중에 발생하면 Exception

## try:
##      예외처리할 문구
## except 예외클래스 as e:
##      예외시 할 행동
##      Exception 클래스는 다른 모든 예외 클래스의 조상임, Exception만 쓰면 됨
##          예외 발생시 예외(자식클래스)의 인스턴스가 생성되고, 그 인스턴스를 Exception(부모클래스)에 전달하는 방식

## [finally] - 옵션
##      예외 발생 유무와 상관없이 항상 처리해야 할 로직
## 2중,3중 try문을 사용하지말 것 - 성능 하락

# 디버깅 - 천천히 어디에서 예외(오류)가 발생하는지 확인하기 위해 사용

## F9 - 중단점
## F5 - 실행
## F10 - 한 프로세스 씩
## F11 - 한 줄씩
## Shift + F5 - 디버깅 종료
## 변수 - 현재 변수에 들어있는 값 표시
## 조사식 - 내가 원하는 식을 추적 가능
## 호출스택 - 스택 상황이 어떤지 보여줌

mul = lambda a,b : a*b
div = lambda a,b : a/b

while True :
    op = input('계산할 연산을 입력(*, /, q) : ')
    if op == 'q' : break
    elif op != '*' and op != '/': print('입력이 잘못되었답니다. 나가려면 q 입력'); continue

    while True :
        try :
            x , y = map(int,(input('계산할 숫자 두개 입력, (스페이스바로 분리) : ').split(' ')))
            break
        except Exception as e:
            print(f"{e}잘못된 입력입니다. 스페이스로 분리해주세요 ex) 3 7")
            continue

    if op == '*' : print(f'{x} * {y} = {mul(x,y)}')

    elif op == '/' : 
        try :
            print(f'{x} / {y} = {div(x,y)}')
        except Exception as e:
            print(f"{e} 0으로 나눌 수 없습니다.")
