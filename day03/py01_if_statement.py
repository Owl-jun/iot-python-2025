# py01_if_statement.py

# if문 : 흐름제어의 가장 기본
# if (참 인 조건) :
#   명령문 실행

age = int(input("나이를 입력하세요."))


# 만약에 나이가 19세가 아니면 담배를 살 수 없습니다.
# 조건이 여러개 일때 and , or 로 계속 작성.
if 19 <= age : print("4500원 입니다.")
else : print("나이좀 더 먹고 오너라 ^^")

grade = input("학점 입력 : ").upper()

if grade == 'A' or grade == 'B' :
    print("우수합니다.")
elif grade == 'C' :
    print("턱걸이 합격")
else:
    print("공부좀하자이")
