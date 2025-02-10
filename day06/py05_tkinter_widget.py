# py05_tkinter_widget
# tkinter 위젯 학습용

from tkinter import *

root = Tk()
root.geometry('1280x720')

img = PhotoImage(file='./day06/cat.png')
label = Label(root,image=img)
label.pack(side=BOTTOM)

root.mainloop()