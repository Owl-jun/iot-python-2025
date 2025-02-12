# py02_pygame.py
# PyGame 그래픽표현 (선, 사각형, 원 ...)

import pygame                   
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN
from pygame.draw import *
import sys                      

# define
FWIDTH = 400
FHEIGHT = 400
LEFTCLICK = 1
WHEELCLICK = 2
RIGHTCLICK = 3
SPEED = 200

# 환경설정
pygame.init()
Surface = pygame.display.set_mode((FWIDTH,FHEIGHT)) 
FPSCLOCK = pygame.time.Clock()                      
pygame.display.set_caption('Pygame Basic')          
pygame.key.set_repeat(500,50)

# 이미지 로드
snake = pygame.image.load('./day08/snake.png')

# 디자인 객체 생성
charactor = pygame.Rect(0,0,10,10)
monster = pygame.Rect(FWIDTH/2,FHEIGHT/2,20,20)
def main():

    # 텍스트 변수
    myfont = pygame.font.SysFont('NanumGothic', 24)
    message1 = myfont.render('This is my message', True,'black','white')
    while True:
        dt = FPSCLOCK.tick(60) / 1000               # deltatime 설정
        Surface.fill((255,255,255))                 # #FFFFFF
    
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == QUIT:                  # WM_DELETE_WINDOW
                pygame.quit()
                sys.exit()
            # 마우스 버튼을 눌렀을 때
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == LEFTCLICK:  # 왼쪽 버튼
                    print(f"현재 사각형 위치: {charactor.x},{charactor.y}")
                    circle(Surface,'red',(charactor.x,charactor.y),20)
                elif event.button == RIGHTCLICK:  # 오른쪽 버튼
                    print(f"현재 사각형 위치: {charactor.x},{charactor.y}")

        keys = pygame.key.get_pressed()             # 키보드 입력 감지
        # wasd 이동 키 바인딩
        if keys[pygame.K_w]:
            charactor.y -= SPEED * dt
        if keys[pygame.K_s]:
            charactor.y += SPEED * dt
        if keys[pygame.K_a]:
            charactor.x -= SPEED * dt
        if keys[pygame.K_d]:
            charactor.x += SPEED * dt
        
        if charactor.colliderect(monster):
            print('충돌')
                
        # pygame.draw.line(Surface, color ='red', start_pos=(30,30), end_pos=(150,30), width=5)
        # line(Surface, (0,0,255), (30,90), (150,90), 5)
        for x in range(10, 400, 10):
            line(Surface,'black',(x,0),(x,400))
            line(Surface,'black',(0,x),(400,x))
        
        # 사각형
        rect(Surface,'black',charactor)
        rect(Surface,'red',monster)
        # circle(Surface,'red',(charactor.x,charactor.y),20)
        # 원 circle 타원 ellipse

        Surface.blit(snake,(0,0))
        Surface.blit(snake,(0,336), (32,32,32,32))

        # 텍스트
        Surface.blit(message1,(30,280))

        pygame.display.update()                       # 화면 업데이트
        
        # FPSCLOCK.tick(30)                           # 30 FPS 지정 (프레임 고정 방식)
        

if __name__ == "__main__":
    main()