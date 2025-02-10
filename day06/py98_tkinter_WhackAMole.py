import tkinter as tk
import random

class WhackAMole:
    def __init__(self, master):
        self.top = self.loadScore()
        self.master = master
        self.master.title("두더지 잡기 게임")
        self.master.geometry("900x1055")

        # 두더지가 나올 틀을 Frame 을 통해 만들기 3X3 배열
        self.frameList = []
        for i in range(9):
            self.frame = tk.Frame(master,border=2,relief="ridge",width=300,height=300)
            self.frameList.append(self.frame)
        for j in range(3):
            for k in range(3):
                self.index = j*3+k
                self.frameList[self.index].place(x=300*k,y=300*j)
        
        # 스코어 및 시간제한 관련 --------------

        self.score = 0
        self.time_left = 30
        
        self.high_score = tk.Label(master, text=f'현재 1등 점수 : {self.top}', font = ("Arial",24))
        self.high_score.pack()
        self.high_score.place(x=600,y=950)

        self.score_label = tk.Label(master, text="점수: 0", font=("Arial", 24))
        self.score_label.pack(side="bottom")
        
        self.time_label = tk.Label(master, text="남은 시간: 10", font=("Arial", 24))
        self.time_label.pack(side="bottom")
        
        self.start_button = tk.Button(master, text="게임 시작", command=self.start_game, font=("Arial", 24))
        self.start_button.pack(side="bottom")

        # ------------------------------------

        self.mole_image = tk.PhotoImage(file='.\day06\dudeoz.png')
        self.mole_button = tk.Button(master, image=self.mole_image, command=self.whack, width=296, height=296)
        

        self.is_game_active = False

    def start_game(self):
        
        self.score = 0
        self.time_left = 10
        self.is_game_active = True
        self.update_score()
        self.update_time()
        self.move_mole()
        self.countdown()


    # 두더지를 클릭(잡았을때) 동작
    def whack(self):
        if self.is_game_active:
            self.score += 1
            self.update_score()
            self.mole_button.place_forget()  # 두더지를 숨김
            self.master.after(random.randint(0,10) * 200, self.move_mole)  # 0.2초 * 0~10 초 중 무작위의 시간 후에 두더지가 나타남

    def update_highScore(self): self.high_score.config(text=f'현재 1등 점수 : {self.loadScore()}')
    def update_score(self): self.score_label.config(text=f"점수: {self.score}")
    def update_time(self): self.time_label.config(text=f"남은 시간: {self.time_left}")

    def move_mole(self):
        if self.is_game_active:
            # 3x3 그리드에서 랜덤한 위치 선택
            x = random.randint(0, 2) * 300
            y = random.randint(0, 2) * 300
            self.mole_button.place(x=x, y=y)

    def countdown(self):
        if self.time_left > 0 and self.is_game_active:
            self.time_left -= 1
            self.update_time()
            self.master.after(1000, self.countdown)
        else:
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

if __name__ == "__main__":
    root = tk.Tk()
    game = WhackAMole(root)
    root.mainloop()
