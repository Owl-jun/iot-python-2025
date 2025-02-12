# py05_blocks.py
# PyGame 그래픽표현 (선, 사각형, 원 ...)

import pygame                   
import sys                      

# define
FWIDTH = 1000
FHEIGHT = 800
LEFTCLICK = 1
WHEELCLICK = 2
RIGHTCLICK = 3
SPEED = 200

# 환경설정
pygame.init()
Surface = pygame.display.set_mode((FWIDTH,FHEIGHT)) 
FPSCLOCK = pygame.time.Clock()                      
pygame.display.set_caption('Pygame Blocks!!')          
pygame.key.set_repeat(10,10)


def main():
    is_game_start = False
    score = 0
    BLOCK = []
    # 클래스 생성
    # 무지개색 정보
    colors = [(255,0,0),(255,150,0),(255,228,0),(11,201,4),(0,80,255),(0,0,147),(201,0,167)]

    bigFont = pygame.font.SysFont('NanumGothic', 80)
    smallFont = pygame.font.SysFont('NanumGothic', 45)
    M_GAME_TITLE = bigFont.render('GAME START?', True , 'white')
    M_GAME_SUBTITLE = smallFont.render('PRESS SPACE_BAR', True, 'white')
    M_CLEAR = bigFont.render('CLEAR!!',True,'yellow')
    M_FAIL = bigFont.render('FAILED',True,'red')

    while True:
        dt = FPSCLOCK.tick(60) / 1000               # deltatime 설정
        Surface.fill((0,0,0))                 # #FFFFFF
    
        # 이벤트 처리
        for event in pygame.event.get():            # 이벤트처리 기본
            if event.type == pygame.QUIT:                  # WM_DELETE_WINDOW
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                elif event.key == pygame.K_RIGHT:
                    pass
                elif event.key == pygame.K_SPACE:
                    is_game_start = True

        # 게임화면 렌더링
        if is_game_start == False:
            Surface.blit(M_GAME_TITLE,((FWIDTH/2)-(537/2),(FHEIGHT/2)-72))
            Surface.blit(M_GAME_SUBTITLE,((FWIDTH/2)-(390/2),(FHEIGHT/2)+50))
        else: # 게임시작 후 블록을 다 그리고 볼이 움직이도록 처리, 바 도 움직이도록 처리
            Surface.blit(M_CLEAR,(80,280))
        pygame.display.update()                       # 화면 업데이트
        FPSCLOCK.tick(30)                           # 30 FPS 지정 (프레임 고정 방식)
        

if __name__ == "__main__":
    main()