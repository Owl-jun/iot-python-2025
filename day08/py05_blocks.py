# py05_blocks.py
# PyGame 그래픽표현 (선, 사각형, 원 ...)

import pygame                   
import sys                      
import random
import math
import time

# define
FWIDTH = 1000
FHEIGHT = 800

class Block:
    def __init__(self,col,rect,speed = 0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45,45) + 270
    
    def move(self):
        # 볼이 움직이는 x축 값을 계속 계산하려면 x는 
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed

    def draw_E(self):   # 공을 circle이 아니라 ellipse로 생성 (콜리젼 계산편함)
        pygame.draw.ellipse(Surface,self.col,self.rect)
    
    def draw_R(self):   
        pygame.draw.rect(Surface,self.col, self.rect)

# 환경설정
pygame.init()
Surface = pygame.display.set_mode((FWIDTH,FHEIGHT)) 
FPSCLOCK = pygame.time.Clock()                      
pygame.display.set_caption('Pygame Blocks!!')          
pygame.key.set_repeat(10,10)

def main():
    is_game_start = False
    BLOCK = []
    
    # 클래스 생성
    # 무지개색 정보
    colors = [(255,0,0),(255,150,0),(255,228,0),(11,201,4),(0,80,255),(0,0,147),(201,0,167)]

    # 초기에 생성될 블럭 모양


    bigFont = pygame.font.SysFont('NanumGothic', 80)
    smallFont = pygame.font.SysFont('NanumGothic', 45)
    M_GAME_TITLE = bigFont.render('GAME START?', True , 'white')
    M_GAME_SUBTITLE = smallFont.render('PRESS SPACE_BAR', True, 'white')
    M_CLEAR = bigFont.render('CLEAR!!',True,'yellow')
    M_FAIL = bigFont.render('FAILED',True,'red')
    fail_time = None
    while True:
        # 스코어, 스피드 글자.
        dt = FPSCLOCK.tick(60) / 1000               # deltatime 설정
        Surface.fill((0,0,0))                 # #FFFFFF
        
        # 이벤트 처리
        for event in pygame.event.get():            # 이벤트처리 기본
            if event.type == pygame.QUIT:                  # WM_DELETE_WINDOW
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if PADDLE.rect.centerx < 50:
                        PADDLE.rect.centerx = 50
                    else:
                        PADDLE.rect.centerx -= 10
                elif event.key == pygame.K_RIGHT:
                    if PADDLE.rect.centerx > FWIDTH - 50:
                        PADDLE.rect.centerx = FWIDTH - 50
                    else:
                        PADDLE.rect.centerx += 10
                elif event.key == pygame.K_SPACE:
                    is_game_start = True
        

        # 게임화면 렌더링
        if is_game_start == False:

            for y, color in enumerate(colors):
                for x in range(9):
                    BLOCK.append(Block(color,pygame.Rect(x * 80 + 150, y * 40 + 40, 60, 20)))

            Surface.blit(M_GAME_TITLE,((FWIDTH/2)-(537/2),(FHEIGHT/2)-72))
            Surface.blit(M_GAME_SUBTITLE,((FWIDTH/2)-(390/2),(FHEIGHT/2)+50))

            BALL = Block((200,200,0),pygame.Rect(375,500,20,20),20)
            PADDLE = Block((200,200,0),pygame.Rect(375,700,100,30))
            score = 0

        else: # 게임시작 후 블록을 다 그리고 볼이 움직이도록 처리, 바 도 움직이도록 처리

            LenBlock = len(BLOCK) # 63개로 시작하지만 공에 충돌해서 개수가 계속 줄어듦
            BLOCK = [x for x in BLOCK if not x.rect.colliderect(BALL.rect)]
            M_SCORE = smallFont.render(f'SCORE : {score:>4d}',True,'white')
            M_SPEED = smallFont.render(f'SPEED : {BALL.speed}',True,'white')
            Surface.blit(M_SCORE,(20,750))
            Surface.blit(M_SPEED,(FWIDTH - 300, 750))

            # Collision Detection
            if BALL.rect.colliderect(PADDLE.rect):
                BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 100
                
            if len(BLOCK) != LenBlock:
                BALL.dir = -BALL.dir
                BALL.speed += 1
                score += 1

            if BALL.rect.centery < 1000:
                BALL.move()

            if BALL.rect.centerx < 0 or BALL.rect.centerx > FWIDTH-10:
                BALL.dir = 180 - BALL.dir
            elif BALL.rect.centery < 0:
                BALL.dir = -BALL.dir
            
            if BALL.rect.centery > 800:
                Surface.blit(M_FAIL,((FWIDTH/2)-(270/2),(FHEIGHT/2)-72))
                # 타이머가 아직 설정되지 않았다면 현재 시간 저장
                if fail_time is None:
                    fail_time = pygame.time.get_ticks()  # 현재 시간 기록

                # fail_time이 설정된 경우, 3초 후 is_game_start를 False로 변경
                if fail_time is not None and pygame.time.get_ticks() - fail_time > 3000:
                    is_game_start = False
                    fail_time = None  # 타이머 초기화

            
            if len(BLOCK) == 0:
                Surface.blit(M_CLEAR,((FWIDTH/2)-(270/2),(FHEIGHT/2)-72))
                if fail_time is None:
                    fail_time = pygame.time.get_ticks()  # 현재 시간 기록
                # fail_time이 설정된 경우, 3초 후 is_game_start를 False로 변경
                if fail_time is not None and pygame.time.get_ticks() - fail_time > 3000:
                    is_game_start = False
                    fail_time = None  # 타이머 초기화
                is_game_start = False


            BALL.draw_E()
            PADDLE.draw_R()
            for i in BLOCK:
                i.draw_R()

        pygame.display.update()                       # 화면 업데이트
        FPSCLOCK.tick(30)                           # 30 FPS 지정 (프레임 고정 방식)
        

if __name__ == "__main__":
    main()