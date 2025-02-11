import google.generativeai as genai
from tkinter import *
from tkinter.messagebox import *  
from tkinter.scrolledtext import *
from tkinter.font import *

# define
TITLE = '제미나이 챗봇 2.0'
WIDTH = 730
HEIGHT = 450
BORDER = 1
RES = f'{WIDTH}x{HEIGHT}'

class gptClone(Tk):

    # 생성자 오버라이딩
    def __init__(self):
        super().__init__()
        # tk.Tk.__init__(self)
        self._settings()
        self._makeWiget()
        self._setWiget()
        self.textMessage.focus_set()

    # 1. 메인 윈도우 생성
    def _settings(self):
        self.title(TITLE) 
        self.geometry(RES)
        self.iconbitmap('./image/robot.ico')
        self.myFont = Font(family='NanumGothic',size=10)
        self.boldFont = Font(family='NanumGothic',size=10,weight='bold',slant=ITALIC)
        self.protocol('WM_DELETE_WINDOW', self.onClosing)

    # 2. 위젯 객체 생성
    def _makeWiget(self):
        self.inputFrame = Frame(self, border=BORDER, relief="ridge" ,width=WIDTH, height=30, bg='#EFEFEF')  # FRAME
        
        self.textMessage = Text(self.inputFrame, height=1, wrap=WORD, relief="sunken",font = self.myFont)   # Text in Frame
        
        self.sendButton = Button(self.inputFrame, text='전송', bg='green', fg='white',                      # Button in Frame
                    command=self.responseMessage, 
                    relief="raised", font = self.myFont)
        
        self.textResult = ScrolledText(self,wrap=WORD, bg='#000000', fg='#ffffff',font = self.myFont)       # Result in self
        self.textResult.pack(fill=BOTH, expand=True)

    # 3. 위젯 환경 설정
    def _setWiget(self):
        self.inputFrame.pack(side=BOTTOM, fill=BOTH)    

        self.textMessage.bind("<Return>",self.keypress)
        self.textMessage.pack(side=LEFT, padx=15)

        self.sendButton.pack(side=RIGHT, padx=20, pady=5, expand=True)

        self.textResult.tag_configure('user',font=self.boldFont,foreground='yellow')
        self.textResult.tag_configure('ai',font=self.myFont,foreground='limegreen') #89F336
        self.textResult.tag_configure('error',font=self.boldFont,foreground='red')


    # 기타 함수 ------------------------------------------
    def keypress(self,event):
        self.responseMessage()

    def responseMessage(self):
        genai.configure(api_key='AIzaSyA_f08XnRASbUswdZQA40C0xDpQLLpZfJw') # 신청한 API키 : AIzaSyA_f08XnRASbUswdZQA40C0xDpQLLpZfJw
        model = genai.GenerativeModel('gemini-2.0-flash')
        text = self.textMessage.get("1.0","end").replace('\n','').strip()
        # showinfo('결과',text) # 다이얼로그, 모달(Modal) 창
        if text:
            try:
                response = model.generate_content(text)
                result = response.text
                self.textResult.insert(END,f'{text}\n', 'user') # 텍스트 아규먼트
                self.textResult.insert(END,"----------\n")
                self.textResult.insert(END,result, 'ai')
                self.textResult.insert(END,"\n\n")
                self.textMessage.delete("1.0","end")
            except Exception as e:
                self.textResult.insert(END,f'Error:{str(e)}\n\n', 'error')
            finally:
                self.textResult.see(END) # 스크롤 다운

    def onClosing(self):
        if askokcancel('종료확인', '종료하시겠습니까?'):
            self.destroy()


if __name__ == '__main__':
    app = gptClone()
    app.mainloop()

