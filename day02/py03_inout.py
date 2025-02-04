# py03_inout.py
# 화면 입출력

print("출력입니다.")

number = input("나이를 고마 입력하시소") # 입력방법
number = int(number) + 1
print("현재나이는", number)

x, y = input("합산할 두 수를 입력하세요(쉼표로구분) > ").split(",")
result = int(x) + int(y)
print(f"{result}zz")


