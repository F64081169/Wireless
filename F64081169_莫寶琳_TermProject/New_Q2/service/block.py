import pygame
import random 
import math

from service.initial import *
from service.function_BestEffort import *

class BLOCK(pygame.sprite.Sprite):
    def __init__(self,i,j):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(BLOCK_SIZE)
        self.color = (223, 255, 177)
        self.image.fill((223, 255, 177))
        self.rect = self.image.get_rect()

        self.rect.x = (BLOCK_SIZE[0]+ROAD_WIDTH) * i 
        self.rect.y = (BLOCK_SIZE[1]+ROAD_WIDTH) * j 
    
    def update(self):
        return
        