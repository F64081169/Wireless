import pygame
import random 
import math

#禎數
FPS = 30 #加速90倍 原本FPS = 1/3
#速度
SPEED = 1.2 #0.4:50  0.12km/s:2.5km #每三秒走1.2 
#lambda
LAMBDA = 1/4 #1/12 (1sec) -> 1/4 (per 3 sec)
#switch time
TOTAL_SWITCH = 0

CALL_LIST = []
INTERVAL_LIST = []


BLACK = (0,0,0)
WHITE = (255,255,255)

# BLOCK
BLOCKS = []
BLOCK_SPRITE = pygame.sprite.Group()
# BASE STATION
BASE_STATIONS = []
BASE_STATION_SPRITE = pygame.sprite.Group()
COORDINATE = []    
# CAR
CARS = []
CAR_SPRITE = pygame.sprite.Group()

### window size
BLOCK_SIZE = (50,50)
ROAD_WIDTH = 2
WINDOW_SIZE = ( (BLOCK_SIZE[0] + ROAD_WIDTH) * 10 - ROAD_WIDTH , (BLOCK_SIZE[1] + ROAD_WIDTH) * 10 - ROAD_WIDTH )
BASE_STATION_SIZE = (40,40)

screen = pygame.display.set_mode(WINDOW_SIZE)
RUNNING_STATE = True

RATIO = BLOCK_SIZE[0] / 2.5
P_TRANSMIT = 120 #dB
ENTROPY = 25 #dB for entropy
PMin_TRANSMIT = 160 #dB for minimum
P_THREASHOLD = 60 #dB for minimum
##            RED         ORANGE      YELLOW        LIME       GREEN        LIGHT_BLUE    BLUE       NAVY      PURPLE       PINK
COLORS = [(255, 0, 0),(255,165,0),(255, 204, 0),(50,205,50),(0, 128, 0),(130,202,250),(0,131,255),(0,0,128),(128,0,128),(240,120,192)]