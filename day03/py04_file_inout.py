## py04_file_inout.py

## 파일 입출력
# 파일 오픈, 읽고, 쓰고, 닫음


## 파일 경로 : 파일이 컴퓨터상에 들어있는 위치

# 상대경로
# . : 현재 위치한 디렉토리
# .. : 부모 폴더 디렉토리
# 경로 구분자 \ / 다 사용가능

# 상대경로 .
with open('./day03/test.txt', mode='w', encoding='utf-8') as f :
    f.write("파일 쓰기 시작합니다. \n")
    f.write("두번째 줄 작성 시작. \n")
# 절대경로 : f = open('C:/Source/iot-python-2025/day03/test2.txt', mode='w', encoding='utf-8')
# mode : 읽기r, 쓰기w, 추가a, ...
# encoding : 한글만(euc-kr,cp949) , 국제어(utf-8)
# write() , readline() , readlines() , close()


with open('./day03/test.txt', mode='r', encoding='utf-8') as r :
    while True :
        line = r.readline() # 한 줄씩 읽음
        if not line : # 한 줄 읽은 값이 None이면
            break
        print(line, end='')
        print(line.replace('\n',''))

