# py02_pygame.py
# PyGame 그래픽표현 (선, 사각형, 원 ...)

import pygame                   
from pygame.locals import QUIT  
import sys                      

# define
FWIDTH = 640
FHEIGHT = 400

# 기본 변수
pygame.init()
Surface = pygame.display.set_mode((FWIDTH,FHEIGHT)) 
FPSCLOCK = pygame.time.Clock()                      
pygame.display.set_caption('Pygame Basic')          
pygame.key.set_repeat(500,50)

def main():

    while True:
        dt = FPSCLOCK.tick(60) / 1000               
        Surface.fill((255,255,255))                 

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:                
                pygame.quit()
                sys.exit()
            
            # wasd 이동 키 바인딩
            if keys[pygame.K_w]:
                print('w')
            if keys[pygame.K_s]:
                print('s')
            if keys[pygame.K_a]:
                print('a')
            if keys[pygame.K_d]:
                print('d')      
            if keys[pygame.MOUSEBUTTONDOWN]:
                print('click')
            

        
        pygame.display.update()                       
        
        # FPSCLOCK.tick(30)                         
        

if __name__ == "__main__":
    main()