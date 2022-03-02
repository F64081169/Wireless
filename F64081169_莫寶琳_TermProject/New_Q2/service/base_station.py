import pygame
import random 
import math
from service.initial import *
from service.function_BestEffort import *

class BASE_STATION(pygame.sprite.Sprite):
    def __init__(self,i,j):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(BASE_STATION_SIZE)
        color_index = random.randrange(1,11)
        self.color = COLORS[color_index-1]
        self.frequency = color_index * 100
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = ( (BLOCK_SIZE[0]+ROAD_WIDTH) * i) + (BLOCK_SIZE[0]-BASE_STATION_SIZE[0])/2
        self.rect.y = ( (BLOCK_SIZE[1]+ROAD_WIDTH) * j) + (BLOCK_SIZE[1]-BASE_STATION_SIZE[1])/2

        prob = random.randrange(0,4)
        if prob == 0: #left
            self.rect.x = self.rect.x - 2
        elif prob == 1: #right
            self.rect.x = self.rect.x + 2
        elif prob == 2: #up
            self.rect.y = self.rect.y + 2
        elif prob == 3: #down
            self.rect.y = self.rect.y - 2
                    
    def update(self):
        return

