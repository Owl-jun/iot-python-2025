# py96_Yutnori.py

import pygame
import sys

S_WIDTH = 1280
S_HEIGHT = 800

class Board():
    def __init__(self):
        self.color = (255,255,255)
        self.steps = []
        self.special_steps = {5 : [6,20], 10 : [11,25], 22 : [23,27]}
        self.image = pygame.image.load('./TOYPROJECT/py96_bg.webp')
        self.image.set_alpha(60)
        self.create_steps()
   
    def create_steps(self):
        self.backPanel = pygame.Rect((S_WIDTH/2) - ((80*5.5)/2)-30, 20,500,500)
        grid_size = 80  # 발판 간격 설정
        start_x, start_y = (S_WIDTH/2) - ((grid_size*5.5)/2), 50

        positions = [
            # 네모 발판 좌표
            (5,5), (5,4), (5,3), (5,2), (5,1), (5,0),
            (4,0), (3,0), (2,0), (1,0), (0,0), (0,1),
            (0,2), (0,3), (0,4), (0,5), (1,5), (2,5),
            (3,5), (4,5), 
            # 대각선 발판 좌표
            (4,1), (3.2,1.8), (2.5,2.5), (1.8,3.2), (1,4), (1,1), (1.8,1.8), (3.2,3.2), (4,4)
        ]

        for x, y in positions:
            rect = pygame.Rect(start_x + (x * grid_size), start_y + (y * grid_size), 40, 40)
            self.steps.append(rect)

    def draw(self, screen):
        count = 0
        highlight = [0,5,10,15,22]
        pygame.draw.rect(screen,(50,50,50),self.backPanel)
        screen.blit(self.image,(0,0))
        for rect in self.steps:
            if count in highlight: self.color = (165,42,42)
            else : self.color = (255,255,255)
            pygame.draw.rect(screen, self.color, rect)
            count += 1
        

class Player():
    def __init__(self):
        self.create_UI()
        self.titleFont = pygame.font.SysFont('NanumGothic',36)
    
    def create_UI(self):
        xSize = 250
        ySize = 400
        self.player = pygame.Surface((xSize,ySize), pygame.SRCALPHA)
        self.player.fill((250,0,0,128))
        self.computer = pygame.Surface((xSize,ySize), pygame.SRCALPHA)
        self.computer.fill((100,30,150,128))

    get_playerField = lambda self : self.player
    get_computerField = lambda self : self.computer

    def draw(self,screen):
        self.pText = self.titleFont.render('PLAYER',True,'white')
        self.cText = self.titleFont.render('COMPUTER',True,'white')
        screen.blit(self.player, (50, 100))
        self.player.blit(self.pText, (10,0))
        screen.blit(self.computer, (S_WIDTH - 300, 100))
        self.computer.blit(self.cText, (10,0))

        pygame.draw.rect(screen, (255, 255, 255), (50, 100, 250, 400), 3)  # Player 
        pygame.draw.rect(screen, (255, 255, 255), (S_WIDTH - 300, 100, 250, 400), 3)  # Computer 

class Pawn():
    def __init__(self):
        self.create_Pawn()

    def create_Pawn(self):
        self.pPawns = []
        self.cPawns = []
        for i in range(5):
            self.pPawn = pygame.image.load('TOYPROJECT\py96_pPawn.png')
            self.pPawns.append(self.pPawn)
            self.cPawn = pygame.image.load('TOYPROJECT\py96_cPawn.png')
            self.cPawns.append(self.cPawn)

    def draw(self,screen,pawns):
        i, grid, start = 0, 50, 100
        for pawn in pawns:
            screen.blit(pawn,(start,start + i * grid))
            i += 1

class Yut():
    def __init__(self):
        self.create_Yut()
    
    def create_Yut(self):
        self.YutFronts = []
        self.YutBacks = []
        for i in range(4):
            self.YutFront = pygame.image.load('TOYPROJECT\yutFront.png')
            self.YutFronts.append(self.YutFront)
            self.YutBack = pygame.image.load('TOYPROJECT\yutBack.png')
            self.YutBacks.append(self.YutBack)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('즐거운 윷놀이 게임')
FPS = pygame.time.Clock()

# 실행
def run():
    BOARD = Board()
    PLAYER = Player()
    PAWN = Pawn()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
        
        # RENDER YOUR GAME HERE
        screen.fill((0,0,0))
        BOARD.draw(screen)
        PLAYER.draw(screen)
        PAWN.draw(PLAYER.get_playerField(),PAWN.pPawns)
        PAWN.draw(PLAYER.get_computerField(),PAWN.cPawns)
        pygame.display.flip()
        deltaTime = FPS.tick(60) / 1000


if __name__ == "__main__" :
    run()