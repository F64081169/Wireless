import pygame
import random 
import math
import matplotlib.pyplot as plt

from function_minimum import *

pygame.init()
pygame.display.set_caption("Q2 Minimum")

if __name__ == "__main__":
    
    screen = pygame.display.set_mode(WINDOW_SIZE)
    ###開始計時
    print("P_TRANSMIT(dB):",P_TRANSMIT)
    print("Lambda:1/12(sec) speed:0.02(km/sec) FPS = 30")
    start = pygame.time.get_ticks()

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
        screen.fill(WHITE)
        BLOCK_SPRITE.draw(screen)
        BASE_STATION_SPRITE.draw(screen)
        CAR_SPRITE.draw(screen)
        
        # UPDATE
        UPDATE()
        BLOCK_SPRITE.update()
        BASE_STATION_SPRITE.update()
        CAR_SPRITE.update()
        pygame.display.update()
    pygame.quit()
    
    figure,axes = plt.subplots(2,1,tight_layout=True)
    figure.canvas.manager.set_window_title("NORMAL DITRIBUTION")
    axes[0].hist(CALL_LIST , bins=100)
    axes[0].set_title("CALLS PER HOUR")
    axes[1].hist(INTERVAL_LIST , bins=100)
    axes[1].set_title("AVERAGE CALL TIME")
    plt.show()