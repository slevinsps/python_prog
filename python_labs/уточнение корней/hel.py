import pygame
from pygame import *
import math
import time





def helecopter(surface, counter_big,teta, counterx, countery):
    pygame.draw.ellipse(screen, Color("black"),Rect(counterx,countery, 150,90), 2)
    pygame.draw.lines(screen, Color("black"),False,
                      ( (counterx,countery+45),(counterx+50,countery+45),(counterx+50,countery+3)),2)

    pygame.draw.lines(screen, Color("black"),False,
                      ( (counterx+75,countery),(counterx+75,countery-20)),2)
    
    counter_big1 = -counter_big
    pygame.draw.lines(screen, Color("black"),False,
                      ( (counterx+13+counter_big,countery-20),(counterx+137+counter_big1,countery-20)),2)

    pygame.draw.lines(screen, Color("black"),False,
                      ( (counterx+60,countery+87),(counterx+60,countery+100)),2)

    pygame.draw.lines(screen, Color("black"),False,
                      ( (counterx+90,countery+87),(counterx+90,countery+100)),2)

    pygame.draw.lines(screen, Color("black"),False,
                      ( (counterx+5,countery+100),(counterx+150,countery+100)),2)
    
    pygame.draw.arc(screen,Color("black"),[counterx-2,countery+83,15,18], 2*math.pi/2, 3*math.pi/2, 2)


    pygame.draw.arc(screen,Color("black"),[counterx+75,countery-45,150,90], 3*math.pi/2, 2*math.pi, 2)


    Xc = counterx+225
    Yc = countery  
    x = counterx+205
    y = countery
    x1 = Xc + (x-Xc)*math.cos(teta) + (y-Yc)*math.sin(teta)
    y1 = Yc + (y-Yc)*math.cos(teta) - (x-Xc)*math.sin(teta)
    xx = counterx+245
    yy = countery
    xx1 = Xc + (xx-Xc)*math.cos(teta) + (yy-Yc)*math.sin(teta)
    yy1 = Yc + (yy-Yc)*math.cos(teta) - (xx-Xc)*math.sin(teta)
    pygame.draw.lines(screen, Color("black"),False, ((x1, y1),(xx1, yy1)), 2)






SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
DISPLAY = (SCREEN_WIDTH,SCREEN_HEIGHT)		
											 
pygame.init()	
screen = pygame.display.set_mode(DISPLAY)	
pygame.display.set_caption('helicopter')		


done = False
clock = pygame.time.Clock()
bg = Surface(DISPLAY)	 
bg.fill(Color("white"))
                             


counter_big = 0
k = 2
teta = 0
x = 2*math.pi
xc = SCREEN_WIDTH // 2
yc = SCREEN_HEIGHT // 2
m = xc /(2*math.pi)
a = 100
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  

    screen.blit(bg, (0,0)) 

    counter_big+=k
    if counter_big == 60:
        k = -2
    if counter_big == 0:
        k = 2
    teta += 0.1
    x = x - 0.05
    counterx = xc+round(x*m);
    countery = yc-round(math.sin(x)*a);

    helecopter(screen,counter_big,teta,counterx,countery)
    if x < -2*math.pi-5:
        x = 2*math.pi
    
    pygame.display.flip()
    clock.tick(60)



pygame.quit()








