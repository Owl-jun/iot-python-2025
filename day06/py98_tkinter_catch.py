from tkinter import *
import tkinter.font as fnt
import random

def catch(event):
    global score
    score += 1
    score_label.config(text=f'현재 score = {score}')
    hide_mole()  # 두더지를 클릭하면 사라지게 함

def show_mole():
    hide_mole()  # 이전 두더지를 숨김
    ranInt = random.randint(0, 8)  # 0부터 8까지의 랜덤 인덱스
    i_List[ranInt].grid(column=ranInt % 3, row=ranInt // 3)  # 두더지 표시
    main.after(2000, hide_mole)  # 2초 후에 사라지게 함

def hide_mole():
    for image in i_List:
        image.grid_forget()  # 두더지 숨기기
    main.after(1000, show_mole)  # 1초 후에 다시 두더지 나타나게 함

main = Tk()
main.title('두더지잡기!')
main.geometry('900x1000')

myfont = fnt.Font(family='NanumGothic', size=20)
ranInt = random.randint(1,100)
i_List = []
ni_List = []
score = 0

score_label = Label(main, text=f'현재 score = {score}', font=myfont)
score_label.grid(column=0, row=4, columnspan=3)

img = PhotoImage(file='./day06/dudeoz.png')

# 두더지 넣을 프레임 생성 3x3 = 9개
for idx in range(9):
    image = Label(main,image=img)
    image.bind('<Button-1>',catch)
    i_List.append(image)

for idx in range(9):
    frame = Frame(main, borderwidth=5, relief="ridge", width=300,height=300)
    frame.bind('<Button-1>',catch)
    ni_List.append(frame)

# 프레임 배치 3x3 grid 활용
if ranInt > 90 :
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            i_List[index].grid(column=j,row=i)
else :
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            ni_List[index].grid(column=j,row=i)

show_mole()

main.mainloop()