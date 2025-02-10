from tkinter import *
import tkinter.font as fnt

main = Tk()
main.geometry('600x200')
main.title('카운트 예제') # 윈도우 창 제목변경

# 이벤트
count = 0   # 계속 증가시킬 수를 담는 변수

def countUp():
    global count
    count += 1
    l['text'] = f'버튼 클릭: {count}'

def countInit():
    global count
    count = 0
    l['text'] = '버튼 클릭: 0'

myfont = fnt.Font(family='NanumGothic', size=20)

# 숫자카운트를 표시할 라벨
l = Label(main, text = '버튼 클릭: 0', fg='blue', font=myfont)
# side = LEFT, TOP, RIGHT, BOTTOM
l.pack(side=TOP, pady=20)

# 버튼 추가 , command 파라미터 - 이벤트 함수 정의
buttonUp = Button(main, text = '카운트 증가', font = myfont, command = countUp)
buttonUp.pack(side=LEFT,padx=20,pady=20)
buttonInit = Button(main, text='초기화', font = myfont, command = countInit)
buttonInit.pack(side=LEFT,padx=20,pady=20)

main.mainloop()