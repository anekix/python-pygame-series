def rectangle(xywh, color, border=0):
    pygame.draw.rect(screen, color, xywh, border)
from pygame.locals import *
lightblue=(0,174,255)
import pygame
map=\
[
"...XX..XXX.....XXXX",
"XXX.....xx....xxxxx",
".........xxxxxxxx..",
"...XX..XXX.....XXXX",
"XXX.....xx....xxxxx",
".........xxxxxxxx..",
"XXX.....xx....xxxxx",
".........xxxxxxxx..",
"...XX..XXX.....XXXX"
 ]
def add():
    map.extend('x')

def create_map():
    cn=1
    y=0
    for i in map:
        for tile in i:
            if tile==".":
                rectangle((cn*20,y,20,20),(255,random.randint(1,255),0))
                cn+=1
            else:
                rectangle((cn*20,y,20,20),(random.randint(100,255),0,255))
                cn+=1
        y+=20
        cn=1
            

import random
pygame.init()
screen = pygame.display.set_mode((800, 300),pygame.FULLSCREEN)
done = False
screen.fill(lightblue)
clock=pygame.time.Clock()
def music():
    pygame.mixer.music.load('ms.wav')
    pygame.mixer.music.play(0)
#rectangle((0,0,20,50),(255,0,0),2)

#create_map()        
while not done:
        clock.tick(30)
        create_map()
        for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN :
                    music()
                    #add()
                if event.type == pygame.QUIT:
                    done = True
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        quit()
        pygame.display.flip()
        
