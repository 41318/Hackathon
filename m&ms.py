import pygame
import math
import random
from pygame.locals import *
import sys
import os

pygame.init()
pygame.time.set_timer(USEREVENT, 2000)
screen = pygame.display.set_mode((520, 695))
done = False
clock = pygame.time.Clock()

roadspeed=0
place = [112,176,240,304,368]



img1=pygame.image.load("/Users/madiar/Desktop/sources/car01.png")
img1=pygame.transform.scale(img1, (40, 80))
img2=pygame.image.load("/Users/madiar/Desktop/sources/block01.png")
img2=pygame.transform.scale(img2, (40, 40))
img3=pygame.image.load("/Users/madiar/Desktop/sources/start.png")
img3=pygame.transform.scale(img3, (96, 40))

class Car():
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
class Block():
	def __init__(self,x,y):
		self.x = x
		self.y = y

blocks = []
blockspeed = 4
a=[]
direction = ""

car = Car(place[2],500)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    k = pygame.time.get_ticks()%2000
    print(k)
    screen.fill((65, 65, 65))

    screen.blit(img1,(car.x,car.y))
    screen.blit(img3,(212,roadspeed))

    if direction=="left":
        car.x-=64
        direction=""
    elif direction=="right":
        car.x+=64
        direction=""


    if 1300<k<1340:
        r=random.randint(0,4)
        a.append(r)
        a=list(dict.fromkeys(a))
        for i in a:
            block = Block(place[i],0)
            blocks.append(block)
            
        
    
    for block in blocks:
        screen.blit(img2,(block.x,block.y))
        block.y+=blockspeed
        if block.y>700:
            blocks.remove(block)
            a=[]

        if block.x==car.x and (car.y-block.y)<45:
            roadspeed=0
            blockspeed=0
            python = sys.executable
            os.execl(python, python, * sys.argv)

        if block.x==car.x and (car.y-block.y)<120:
            direction="right"



    #jol
    pygame.draw.line(screen, (255,255,255),(98,0),(98,700),3)
    pygame.draw.line(screen, (255,255,255),(422,0),(422,700),3)

    for i in range(163,419,64):
    	for j in range(0,720,20):
    		if ((j+roadspeed+10)%700-(j+roadspeed)%700)<0:
    			pygame.draw.line(screen, (255,255,255),(i,0),(i,(j+roadspeed+10)%700),3)
    		else:
        		pygame.draw.line(screen, (255,255,255),(i,(j+roadspeed)%700),(i,(j+roadspeed+10)%700),3)

    roadspeed+=4

    pygame.display.flip()
    clock.tick(40)