import pygame
import random 
import math
from service.initial import *
 
def overlap(time1,time2):
    if time1[0] <= time2[1] and time1[1] >= time2[0]:
        return True
    else:
        return False

def calls_per_hour():
    while True:
        x = round( random.gauss(mu = 2, sigma = 2) )
        if x >= 0:
            break
    return x
def time_intervals(n):
    times = []
    for i in range(n):
        if i == 0:
            period = random.gauss(mu = 180, sigma = 40)
            period = round(period)
            start_time = random.randrange(0,3600)
            end_time = start_time + period
            time = (start_time, end_time)
            times.append(time)
            INTERVAL_LIST.append(period)
    else:
        while True:
            count = 0
            period = random.gauss(mu = 180, sigma = 40)
            period = round(period)
            start_time = random.randrange(0,3600)
            end_time = start_time + period
            if end_time >= 3600:
                continue
            new_time = (start_time,end_time)
            for time in times:
                if overlap(time,new_time) == False:
                    count += 1
            if(count == len(times)):
                times.append(new_time)
                INTERVAL_LIST.append(period)
                break                
    times.sort(key = lambda x: x[0])
    return times


class CAR(pygame.sprite.Sprite):           
    def __init__(self,i,j,direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((ROAD_WIDTH,ROAD_WIDTH))
        self.current_base_station = -1
        self.color = BLACK
        self.image.fill(self.color)
        self.rect = self.image.get_rect()  
        self.rect.x = i
        self.rect.y = j
        self.direction = direction
        self.P_RECEIVE = float("-inf")
        # new variables
        self.time_count = 0
        self.calls = 0
        self.time_intervals = []
        self.connect = False
                        
    def check_turn(self,x,y):
        for i in range(10):
            for j in range(10):
                car_x = ( (BLOCK_SIZE[0] + ROAD_WIDTH) * i) + BLOCK_SIZE[0]
                car_y = ( (BLOCK_SIZE[1] + ROAD_WIDTH) * j) + BLOCK_SIZE[1]
                if car_x == x and car_y == y:
                    return 1
        return 0
        
    def update(self):
        global CALL_LIST
        if self.time_count == 0:
            self.calls = calls_per_hour()
            self.time_intervals = time_intervals(self.calls)
            CALL_LIST.append(self.calls)
       
        check = self.check_turn(self.rect.x,self.rect.y)
        if check == 1:
            prob = random.randint(1,32)
            if prob <= 16:
                self.direction = self.direction + 0
            elif prob >= 17 and prob <= 18:
                self.direction = self.direction + 2 
            elif prob >= 19 and prob <= 26:
                self.direction = self.direction + 1
            else:
                self.direction = self.direction - 1
            self.direction = self.direction % 4
        
        if self.direction == 0:
            self.rect.y += SPEED
        elif self.direction == 1:
            self.rect.y -= SPEED
        elif self.direction == 2:
            self.rect.x += SPEED
        elif self.direction == 3:
            self.rect.x -= SPEED
        
        self.time_count += 1
        if len(self.time_intervals) > 0:
            if self.time_count == self.time_intervals[0][0]:
                self.color = self.color
                self.connect = True
                #print("connect")
            if self.time_count == self.time_intervals[0][1]:
                self.color = BLACK
                self.connect = False
                self.calls -= 1
                del(self.time_intervals[0])
                #print("disconnect")
        if self.time_count == 3600:
            self.time_count = 0

        self.image.fill(self.color)