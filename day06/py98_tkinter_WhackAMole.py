import tkinter as tk
import random

RES = "900x1055"
WIDTH = 300
HEIGHT = 300
BORDER = 2

class WhackAMole:
    def __init__(self, main):

        # 제목설정 및 기초작업
        self.top = self.loadScore()
        self.main = main
        self.main.title("두더지 잡기 게임")
        self.main.geometry(RES)

        # 두더지가 나올 틀(배경)을 Frame 으로 만들기 3X3 배열
        self.frameList = []
        for i in range(9):
            self.frame = tk.Frame(main,border=BORDER,relief="ridge",width=WIDTH,height=HEIGHT)
            self.frameList.append(self.frame)
        for j in range(3):
            for k in range(3):
                self.index = j*3+k      #j = row , k = col
                self.frameList[self.index].place(x=WIDTH*k,y=HEIGHT*j)
        
        # 스코어 및 시간제한 관련 --------------
        self.score = 0
        self.time_left = 30
        
        self.high_score = tk.Label(main, text=f'현재 1등 점수 : {self.top}', font = ("Arial",24))
        self.high_score.pack()
        self.high_score.place(x=WIDTH*2,y=HEIGHT*3)

        self.score_label = tk.Label(main, text="점수: 0", font=("Arial", 24))
        self.score_label.pack(side="bottom")
        
        self.time_label = tk.Label(main, text="남은 시간: 10", font=("Arial", 24))
        self.time_label.pack(side="bottom")
        
        self.start_button = tk.Button(main, text="게임 시작", command=self.start_game, font=("Arial", 24))
        self.start_button.pack(side="bottom")
        # ------------------------------------

        # 두더지 관련 설정
        self.mole_image = tk.PhotoImage(file='.\day06\dudeoz.png')
        self.mole_button = tk.Button(main, image=self.mole_image, command=self.whack, width=WIDTH-(BORDER*2), height=HEIGHT-(BORDER*2))

        self.is_game_active = False
    
    # 람다 연습 겸 , 간단한 함수 람다로 작성하기
    # 게임 정보 업데이트 함수
    update_highScore = lambda self : self.high_score.config(text=f'현재 1등 점수 : {self.loadScore()}')
    update_score = lambda self : self.score_label.config(text=f"점수: {self.score}")
    update_time = lambda self : self.time_label.config(text=f"남은 시간: {self.time_left}")

    # *** 게임 시작 버튼 누르면 동작 ***
    def start_game(self):
        self.score = 0
        self.time_left = 10
        self.is_game_active = True
        self.update_score()
        self.update_time()
        self.move_mole()
        self.countdown()

    # *** 두더지를 클릭(잡았을때) 동작 ***
    def whack(self):
        if self.is_game_active:
            self.score += 1
            self.update_score()
            self.mole_button.place_forget()  # 두더지 잠시 치워버리기
            self.main.after(random.randint(0,10) * 200, self.move_mole)  # 0.2초 * 0~10 초 중 무작위의 시간 후에 두더지가 나타남

    # *** 두더지 랜덤 배치 함수 ***
    def move_mole(self):
        if self.is_game_active:
            # 3x3 그리드에서 랜덤한 위치 선택
            _x = random.randint(0, 2) * 300
            _y = random.randint(0, 2) * 300
            self.mole_button.place(x = _x, y = _y)

    # *** 시간 흐르게 하는 함수 ***
    def countdown(self):
        if self.time_left > 0 and self.is_game_active:
            self.time_left -= 1
            self.update_time()
            self.main.after(1000, self.countdown)
        else:   # 게임 종료
            self.is_game_active = False
            self.mole_button.place_forget()
            self.time_label.config(text="게임 종료!")
            self.score_label.config(text=f"최종 점수: {self.score}")
                # 스코어 기록
            with open('./day06/score.txt',mode='a',encoding='utf-8') as f:
                f.write(f'{self.score}\n')
            self.update_highScore()
    
    # 스코어 기록된 텍스트파일에서 하이스코어 가져오기
    def loadScore(self):
        scoreList = [0]
        with open(file='./day06/score.txt',mode='r',encoding='utf-8') as r:
            while True :
                score = r.readline().replace('\n','')
                if not score: break
                scoreList.append(int(score))
        return max(scoreList)


# --------------------------------------
# --------------------------------------
# --------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    WhackAMole(root)
    root.mainloop()
