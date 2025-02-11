# py01_gpt_clone.py
#
import google.generativeai as genai

from tkinter import *                   # tkinter 모듈에 있는 모든 클래스, 함수, 변수 등을 다 쓰겠다.
from tkinter.messagebox import *        # 모듈 밑에 있는 모듈을 from tkinter import *로 가져올 수 없음
from tkinter.scrolledtext import *
from tkinter.font import *




WIDTH = 730
HEIGHT = 450
BORDER = 1


# 4. 전송 버튼 이벤트
def responseMessage():
    genai.configure(api_key='AIzaSyA_f08XnRASbUswdZQA40C0xDpQLLpZfJw') # 신청한 API키 : AIzaSyA_f08XnRASbUswdZQA40C0xDpQLLpZfJw
    model = genai.GenerativeModel('gemini-2.0-flash')
    text = textMessage.get("1.0","end").replace('\n','').strip()
    # showinfo('결과',text) # 다이얼로그, 모달(Modal) 창
    if text:
        try:
            response = model.generate_content(text)
            result = response.text
            textResult.insert(END,f'{text}\n', 'user') # 텍스트 아규먼트
            textResult.insert(END,"----------\n")
            textResult.insert(END,result, 'ai')
            textResult.insert(END,"\n\n")
            textMessage.delete("1.0","end")
        except Exception as e:
            textResult.insert(END,f'Error:{str(e)}\n\n', 'error')
        finally:
            textResult.see(END) # 스크롤 다운

def keypress(event):
    # print(repr(event.char)) # repr을 안쓰면 \r , \x80 등이 표시안됨
    responseMessage()

# 10. 종료시 이벤트처리 함수
def onClosing():
    if askokcancel('종료확인','종료하시겠습니까?'):
        root.destroy()


# 1. 메인 윈도우 생성
root = Tk()
root.title('제미나이 챗봇')
root.geometry(f'{WIDTH}x{HEIGHT}')
root.iconbitmap('./image/robot.ico')

# 6. 전체에서 사용할 폰트 지정 -> 나눔고딕
myFont = Font(family='NanumGothic',size=10)
boldFont = Font(family='NanumGothic',size=10,weight='bold',slant=ITALIC)
# 2. UI화면 구성
inputFrame = Frame(root, border=BORDER, relief="ridge" ,width=WIDTH, height=30, bg='#EFEFEF')
inputFrame.pack(side=BOTTOM, fill=BOTH)

# 3. inputFrame에 들어갈 Entry와 Button 구성
textMessage = Text(inputFrame, height=1, wrap=WORD, relief="sunken",font = myFont)
textMessage.bind("<Return>",keypress)
textMessage.pack(side=LEFT, padx=15)

sendButton = Button(inputFrame, text='전송', bg='green', fg='white', 
                    command=responseMessage, 
                    relief="raised", font = myFont)
sendButton.pack(side=RIGHT, padx=20, pady=5, expand=True)

# 5. API호출 결과메시지 출력될 스크롤기능 텍스트위젯
textResult = ScrolledText(root,wrap=WORD, bg='#000000', fg='#ffffff',font = myFont)
textResult.pack(fill=BOTH, expand=True)

# 8. 스크롤 텍스트에 나올 메시지 디자인
textResult.tag_configure('user',font=boldFont,foreground='yellow')
textResult.tag_configure('ai',font=myFont,foreground='limegreen') #89F336
textResult.tag_configure('error',font=boldFont,foreground='red')

# 7. 실행 후 바로 입력창에 포커스가 가도록
textMessage.focus_set()

# 9. 프로그램 종료버튼 X 를 누르면 종료메시지 확인 후 종료
root.protocol('WM_DELETE_WINDOW', onClosing)


# 1. 종료시 까지 계속 돈다
root.mainloop()