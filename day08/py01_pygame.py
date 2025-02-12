# py01_pygame.py

import pygame                   # pygame 기본모듈 추가
from pygame.locals import QUIT  # 종료처리 변수
import sys                      # 운영체제 시스템 명령

# define
FWIDTH = 640
FHEIGHT = 400

# 기본 변수
pygame.init()
Surface = pygame.display.set_mode((FWIDTH,FHEIGHT)) # 디스플레이 크기 설정
FPSCLOCK = pygame.time.Clock()                      # FPS
pygame.display.set_caption('Pygame Basic')          # 제목 설정
pygame.key.set_repeat(500,50)

def main():

    while True:
        dt = FPSCLOCK.tick(60) / 1000
        Surface.fill((255,255,255))                 # #FFFFFF

        for event in pygame.event.get():
            if event.type == QUIT:                  # WM_DELETE_WINDOW
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(pygame.KEYDOWN)
            elif event.type == pygame.KEYUP:
                print(pygame.KEYUP)
        
        pygame.display.update()                       # 화면 업데이트
        
        # FPSCLOCK.tick(30)                           # 30 FPS 지정 (프레임 고정 방식)
        

if __name__ == "__main__":
    main()