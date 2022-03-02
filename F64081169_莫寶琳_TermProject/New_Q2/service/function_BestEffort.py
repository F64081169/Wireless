import pygame
import random 
import math
from service.initial import *
from service.block import BLOCK
from service.car import CAR
from service.base_station import BASE_STATION

def CHECK_DUPLICATE(i,j,list):
    for k in range(len(list)):
        if i == list[k][0] and j == list[k][1]:
            return 1
    return 0
        
def draw_text(text, size, x, y, color):
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    screen.blit(text_surface, text_rect)
    
def draw_line(color, start, end, width):
    pygame.draw.line(screen , color , start , end , width)  
    
def calculate_distance(car_x,car_y,base_station_x,base_station_y):
    delta_x_square = (car_x - base_station_x)**2
    delta_y_square = (car_y - base_station_y)**2
    result = (delta_x_square + delta_y_square)**(1/2)
    result = result / RATIO
    return result

def calculate_path_loss(frequency, distance):
    result = 32.45 + (20 * math.log10(frequency)) + (20 * math.log10(distance))
    return result

def check_in_map(left,right,top,bottom):
    if (right <= 0) or (left >= WINDOW_SIZE[0]) or (top >= WINDOW_SIZE[1]) or (bottom <= 0):
        return 0
    else:
        return 1
    
def determine_base_station(car,BASE_STATIONS): #determine the largest power of base station to connect
    P_RECEIVE = 0
    LARGEST = float("-inf")
    index = -1
    for j in range(len(BASE_STATIONS)):
        base_station = BASE_STATIONS[j]
        frequency = base_station.frequency
        distance = calculate_distance(car.rect.centerx , car.rect.centery , base_station.rect.centerx , base_station.rect.centery)
        path_loss = calculate_path_loss(frequency,distance)
        P_RECEIVE = P_TRANSMIT - path_loss

        if P_RECEIVE > LARGEST:
            LARGEST = P_RECEIVE
            index = j

    P_RECEIVE = LARGEST
    color = BASE_STATIONS[index].color
    car.P_RECEIVE = P_RECEIVE
    return index , P_RECEIVE , color

def arrival_probability():
    probability = ((LAMBDA * 1) ** 1) * (math.e ** -(LAMBDA * 1))
    probability = round(probability, 7) * (10**7)
    return probability

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

def CREATE_BLOCK_AND_BASE_STATION():
    for i in range(10):
        for j in range(10):
            block_temp = BLOCK(i,j)
            BLOCKS.append(block_temp)
            BLOCK_SPRITE.add(block_temp)
            prob = random.randrange(0,10)
            if(prob == 1):
                if ( CHECK_DUPLICATE(i,j,COORDINATE) == 0 ):
                    COORDINATE.append( (i,j) )
                    base_station_temp = BASE_STATION(i,j)
                    BASE_STATIONS.append(base_station_temp)
                    BASE_STATION_SPRITE.add(base_station_temp)

def CREATE_CAR():        
    for i in range(4):
        for j in range(0,10):
            arrival_prob = arrival_probability()
            prob = random.randrange(0 , 10**7)
            
            if(i == 0): # DOWN
                if prob < arrival_prob:
                    x = ( (BLOCK_SIZE[0] + ROAD_WIDTH) * j ) + BLOCK_SIZE[0]
                    y = 0
                    car_temp = CAR(x,y,0)
                    index , P_RECEIVE , color = determine_base_station(car_temp,BASE_STATIONS)
                    car_temp.color = BLACK
                    car_temp.current_base_station = index
                    CARS.append(car_temp)
                    CAR_SPRITE.add(car_temp)
            elif(i == 1): # UP
                if prob < arrival_prob:
                    x = ( (BLOCK_SIZE[0] + ROAD_WIDTH) * j ) + BLOCK_SIZE[0]
                    y = ( BLOCK_SIZE[1] + ROAD_WIDTH ) * 10 - 1/4*BLOCK_SIZE[1]
                    car_temp = CAR(x,y,1)
                    index , P_RECEIVE , color = determine_base_station(car_temp,BASE_STATIONS)
                    car_temp.color = BLACK
                    car_temp.current_base_station = index
                    CARS.append(car_temp)
                    CAR_SPRITE.add(car_temp)
            elif(i == 2): # RIGHT
                if prob < arrival_prob:
                    x = 0 
                    y = ( (BLOCK_SIZE[1] + ROAD_WIDTH) * j ) + BLOCK_SIZE[1]
                    car_temp = CAR(x,y,2)
                    index , P_RECEIVE , color = determine_base_station(car_temp,BASE_STATIONS)
                    car_temp.color = BLACK
                    car_temp.current_base_station = index
                    CARS.append(car_temp)
                    CAR_SPRITE.add(car_temp)
            elif(i == 3): # LEFT
                if prob < arrival_prob:
                    x = ( BLOCK_SIZE[0] + ROAD_WIDTH ) * 10 - 1/4*BLOCK_SIZE[0]
                    y = ( (BLOCK_SIZE[1] + ROAD_WIDTH) * j ) + BLOCK_SIZE[1]
                    car_temp = CAR(x,y,3)
                    index , P_RECEIVE , color = determine_base_station(car_temp,BASE_STATIONS)
                    car_temp.color = BLACK
                    car_temp.current_base_station = index
                    CARS.append(car_temp)
                    CAR_SPRITE.add(car_temp)

def UPDATE():
    global TOTAL_SWITCH
    for car in CARS:
        if check_in_map(car.rect.left , car.rect.right , car.rect.top , car.rect.bottom) == 0:
            car.kill()
            CARS.remove(car)            
    
    for base_station in BASE_STATIONS:
        text = str(base_station.frequency) + " MHZ"
        draw_text(text , 11 , base_station.rect.centerx , base_station.rect.centery , WHITE)

    for i in range(len(CARS)):
        car = CARS[i]
        if car.connect == True:
            old_index = car.current_base_station
            new_index , P_receive , color = determine_base_station(car,BASE_STATIONS)
            car.current_base_station = new_index
            car.color = color
            
            P_receive = round(P_receive,2)     
            text = str(P_receive) + " dB"
            # car_pos = (car.rect.centerx , car.rect.centery)
            # base_station_pos = ( BASE_STATIONS[new_index].rect.centerx , BASE_STATIONS[new_index].rect.centery)
            # draw_line(car.color , car_pos , base_station_pos , 1)
            # draw_text(text , 14 , car.rect.x+10 , car.rect.y-10 , car.color)
            if(new_index != old_index):
                TOTAL_SWITCH = TOTAL_SWITCH + 1
                print("TOTAL SWITCH : ",TOTAL_SWITCH,"CAR NUM : ",len(CARS))


