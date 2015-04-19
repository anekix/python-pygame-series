#code by: "kshitijkumar singh"

import pygame

#Block class to handle drawing and updation of blocks on screen
class Block():

    def __init__(self,color,w,h):
        self.background = pygame.Surface((w,h))
        self.background.fill(color)
        self.xn=screen_size[0]/2
        self.yn=screen_size[1]/2

    def draw(self,canvas):
        canvas.blit(self.background, (self.xn,self.yn))

    def update(self,xx,yy):
        self.xn=xx
        self.yn=yy

#global varuiable for game loop       
done=True
#initialize pygame and create a screen canvas to draw upon
pygame.init()
screen_size=(640,480)
screen=pygame.display.set_mode(screen_size)
#used to set the frame rate
clock=pygame.time.Clock()

#positions where block will be drawn,this will be updated
#to make the block move based on user input
xin=640/2
yin=480/2
#by default the key-repeat event is disabeled.enable it
pygame.key.set_repeat(50, 50)
block=Block((255,0,0),20,20)     
block.draw(screen)

while done == True:
    
    block.draw(screen) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                xin-=10
                block.update(xin,yin)
                block.draw(screen)
                
            if event.key==pygame.K_RIGHT:
                xin+=10
                block.update(xin,yin)
                block.draw(screen)
            if event.key==pygame.K_UP:
                yin-=10
                block.update(xin,yin)
                block.draw(screen)
            if event.key==pygame.K_DOWN:
                yin+=10
                block.update(xin,yin)
                block.draw(screen)
            
            
    
    pygame.display.update()
    clock.tick(60)
    screen.fill((255,255,255))
pygame.quit()
