import pygame
import random 
import math
from service.function_My import UPDATE,CREATE_BLOCK_AND_BASE_STATION,CREATE_CAR
from service.Initial import *
import matplotlib.pyplot as plt


#禎數
FPS = 30 #加速90倍 原本FPS = 1/3
#速度
SPEED = 1.2 #0.4:50  0.12km/s:2.5km #每三秒走1.2 
#lambda
LAMBDA = 1/4 #1/12 (1sec) -> 1/4 (per 3 sec)

pygame.init()
pygame.display.set_caption("Q1 My_Algo")


if __name__ == "__main__":
    ###開始計時
    start = pygame.time.get_ticks()
    ###初始化
    print("P_TRANSMIT(dB):",P_TRANSMIT)
    print("Lambda:1/12(sec) speed:0.02(km/sec) FPS = 30")
    CREATE_BLOCK_AND_BASE_STATION()
    print(len(BASE_STATIONS))
    # GAME LOOP
    while RUNNING_STATE == True:
        end = pygame.time.get_ticks() -start 
        if end > 30*1000:#計時30秒
            RUNNING_STATE = False
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING_STATE = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    RUNNING_STATE = False
        # CAR
        CREATE_CAR()
        
        # 畫面顯示
        screen.fill((255,255,255)) ###White
        BLOCK_SPRITE.draw(screen)
        BASE_STATION_SPRITE.draw(screen)
        CAR_SPRITE.draw(screen)
        
        # UPDATE
        BLOCK_SPRITE.update()
        BASE_STATION_SPRITE.update()
        CAR_SPRITE.update()
        UPDATE()
        pygame.display.update()
        
    pygame.quit()

