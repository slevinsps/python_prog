import pygame
from pygame import *
import math
import time





def sun(surface, counter, counterx, countery):
        color = (255, 255, 0) # yellow 
        
        num_points = 10
        point_list = []
        center_x = counterx
        center_y = countery
        for i in range(num_points * 2):
                radius = 70
                if i % 2 == 0:
                        radius = radius // 2
                ang = i * math.pi / num_points + counter * math.pi / 120
                x = center_x + int(math.cos(ang) * radius)
                y = center_y + int(math.sin(ang) * radius)
                point_list.append((x, y))
        pygame.draw.polygon(surface, color, point_list)

def star(surface,K,counterx, countery):
        color = (255, 255, 0) # yellow 
        
        num_points = 5
        point_list = []
        center_x = counterx
        center_y = countery
        for i in range(num_points * 2):
                radius = 5
                if i % 2 == 0:
                        radius = radius // 2
                ang = i * 3.14159 / num_points
                x = center_x + int(math.cos(ang) * radius)
                y = center_y + int(math.sin(ang) * radius)
                x1 = center_x * (1-K) + K * x
                y1 = center_y * (1-K) + K * y
                point_list.append((x1, y1))
        pygame.draw.polygon(surface, color, point_list)


        
def cloud(surface, counterx,countery):
    pygame.draw.ellipse(screen, Color("white"),
                        Rect(counterx,countery, 50,30), 0)
    pygame.draw.ellipse(screen, Color("white"),
                        Rect(counterx+20,countery-10, 50,30), 0)   
    pygame.draw.ellipse(screen, Color("white"),
                        Rect(counterx+30,countery+5, 60,40), 0)
    pygame.draw.ellipse(screen, Color("white"),
                        Rect(counterx+50,countery-20, 70,60), 0)
    pygame.draw.ellipse(screen, Color("white"),
                        Rect(counterx+70,countery-10, 80,60), 0)
    pygame.draw.ellipse(screen, Color("white"),
                        Rect(counterx+90,countery-10, 90,50), 0)


def aircraft(surface, counterx,countery):
    k = 2
    pygame.draw.polygon(screen, Color("brown"),
                      ( (counterx,countery),(counterx,countery+20*k),(counterx+20*k,countery+40*k),(counterx+110*k,countery+40*k),
                        (counterx+90*k,countery+20*k),(counterx+20*k,countery+20*k)))
    pygame.draw.polygon(screen, Color("black"),
                      ( (counterx,countery),(counterx,countery+20*k),(counterx+20*k,countery+40*k),(counterx+110*k,countery+40*k),
                        (counterx+90*k,countery+20*k),(counterx+20*k,countery+20*k)),2)
    pygame.draw.polygon(screen, Color("brown"), 
                      ( (counterx+30*k,countery),(counterx+50*k,countery),(counterx+70*k,countery+20*k),(counterx+50*k,countery+20*k)))
    pygame.draw.polygon(screen, Color("black"), 
                      ( (counterx+30*k,countery),(counterx+50*k,countery),(counterx+70*k,countery+20*k),(counterx+50*k,countery+20*k)),2)
    pygame.draw.polygon(screen, Color("brown"),
                      ( (counterx+50*k,countery+30*k),(counterx+70*k,countery+30*k),(counterx+40*k,countery+60*k),(counterx+20*k,countery+60*k)))
    pygame.draw.polygon(screen, Color("black"),
                      ( (counterx+50*k,countery+30*k),(counterx+70*k,countery+30*k),(counterx+40*k,countery+60*k),(counterx+20*k,countery+60*k)),2)
    pygame.draw.polygon(screen, Color("white"), 
                      ( (counterx+90*k,countery+20*k),(counterx+90*k,countery+30*k),(counterx+100*k,countery+30*k)))
    pygame.draw.polygon(screen, Color("black"), 
                      ( (counterx+90*k,countery+20*k),(counterx+90*k,countery+30*k),(counterx+100*k,countery+30*k)),2)
 
def road(surface,w,h):
    pygame.draw.rect(surface, Color("grey"), Rect(0, h, w, 200), 0)
    pygame.draw.rect(surface, Color("white"), Rect(0, h+98, w, 5), 0)
    
def car(surface, counterx, countery, teta, bb1):
    k = 2
    pygame.draw.polygon(screen, Color("red"),
                      ( (counterx,countery),(counterx+7*k,countery-10*k),(counterx+80*k,countery-10*k),
                        (counterx+110*k,countery),(counterx+110*k,countery+20*k),(counterx,countery+20*k)))
    pygame.draw.polygon(screen, Color("black"),
                      ( (counterx,countery),(counterx+20*k,countery-30*k),(counterx+60*k,countery-30*k),(counterx+80*k,countery-10*k),
                        (counterx+110*k,countery),(counterx+110*k,countery+20*k),(counterx,countery+20*k)),2)

    pygame.draw.polygon(screen, Color("black"), 
                      ( (counterx+80*k,countery-10*k),(counterx+60*k,countery-10*k),(counterx+60*k,countery-30*k),
                        (counterx+40*k,countery-30*k),(counterx+40*k,countery-10*k),(counterx+40*k,countery+10*k),
                        (counterx+50*k,countery+10*k),(counterx+60*k,countery-10*k),(counterx+40*k,countery-10*k)),2)

    pygame.draw.polygon(screen, Color("black"),
                      ( (counterx+40*k,countery-10*k),(counterx+40*k,countery-30*k),(counterx+20*k,countery-30*k),(counterx+20*k,countery-10*k),),2)
    pygame.draw.polygon(screen, Color("black"),
                    ((counterx+7*k,countery-10*k),(counterx+20*k,countery-30*k),(counterx+20*k,countery-10*k)),2)

    if not bb1:
        pygame.draw.polygon(screen, Color("yellow"),
                            ( (counterx,countery),(counterx,countery+10*k),(counterx+5*k,countery+10*k),(counterx+5*k,countery+2*k),))
        pygame.draw.polygon(screen, Color("yellow"),
                            ( (counterx+110*k,countery),(counterx+105*k,countery+2*k),(counterx+105*k,countery+10*k),(counterx+110*k,countery+10*k),))
    if bb1:
        pygame.draw.polygon(screen, Color("white"),
                            ( (counterx,countery),(counterx,countery+10*k),(counterx+5*k,countery+10*k),(counterx+5*k,countery+2*k),))
        pygame.draw.polygon(screen, Color("white"),
                            ( (counterx+110*k,countery),(counterx+105*k,countery+2*k),(counterx+105*k,countery+10*k),(counterx+110*k,countery+10*k),))
    pygame.draw.polygon(screen, Color("black"),
                      ( (counterx,countery),(counterx,countery+10*k),(counterx+5*k,countery+10*k),(counterx+5*k,countery+2*k),),2)
    
    pygame.draw.polygon(screen, Color("black"),
                      ( (counterx+110*k,countery),(counterx+105*k,countery+2*k),(counterx+105*k,countery+10*k),(counterx+110*k,countery+10*k),),2)

    pygame.draw.circle(screen, Color("#E68B51"), (counterx+51*k,countery-16*k), 6*k)
    pygame.draw.circle(screen, Color("black"), (counterx+51*k,countery-16*k), 6*k,2)
    
    pygame.draw.circle(screen, Color("#4A4A4A"), (counterx+20*k,countery+20*k), 11*k)
    pygame.draw.circle(screen, Color("black"), (counterx+20*k,countery+20*k), 11*k,2)
    pygame.draw.circle(screen, Color("#A6A6A6"), (counterx+20*k,countery+20*k), 5*k)
    pygame.draw.circle(screen, Color("black"), (counterx+20*k,countery+20*k), 5*k, 2)
    
    Xc = counterx+20*k
    Yc = countery+20*k
    teta = -teta  
    x = (counterx+10*k*1.3)
    y = (countery+10*k*1.3)
    x1 = Xc + (x-Xc)*math.cos(teta) + (y-Yc)*math.sin(teta)
    y1 = Yc + (y-Yc)*math.cos(teta) - (x-Xc)*math.sin(teta)
    xx = (counterx+30*k*0.9)
    yy = (countery+30*k*0.9)
    xx1 = Xc + (xx-Xc)*math.cos(teta) + (yy-Yc)*math.sin(teta)
    yy1 = Yc + (yy-Yc)*math.cos(teta) - (xx-Xc)*math.sin(teta)
    pygame.draw.lines(screen, Color("black"),True, ((x1, y1),(xx1, yy1)), 2)
   
    x = counterx+30*k*0.9
    y = countery+10*k*1.3
    x1 = Xc + (x-Xc)*math.cos(teta) + (y-Yc)*math.sin(teta)
    y1 = Yc + (y-Yc)*math.cos(teta) - (x-Xc)*math.sin(teta)
    xx = counterx+10*k*1.3
    yy = countery+30*k*0.9
    xx1 = Xc + (xx-Xc)*math.cos(teta) + (yy-Yc)*math.sin(teta)
    yy1 = Yc + (yy-Yc)*math.cos(teta) - (xx-Xc)*math.sin(teta)
    
    pygame.draw.lines(screen, Color("black"),True, ((x1, y1),(xx1, yy1)), 2)
    
    
    pygame.draw.circle(screen, Color("#4A4A4A"), (counterx+90*k,countery+20*k), 11*k)
    pygame.draw.circle(screen, Color("black"), (counterx+90*k,countery+20*k), 11*k, 2)
    pygame.draw.circle(screen, Color("#A6A6A6"), (counterx+90*k,countery+20*k), 5*k)
    pygame.draw.circle(screen, Color("black"), (counterx+90*k,countery+20*k), 5*k, 2)




    Xc = counterx+90*k
    Yc = countery+20*k  
    x = counterx+80*k+6

    y = countery+10*k+6
    
    x1 = Xc + (x-Xc)*math.cos(teta) + (y-Yc)*math.sin(teta)
    y1 = Yc + (y-Yc)*math.cos(teta) - (x-Xc)*math.sin(teta)
    
    xx = counterx+100*k-7.6
    yy = countery+30*k-7.6
    
    xx1 = Xc + (xx-Xc)*math.cos(teta) + (yy-Yc)*math.sin(teta)
    yy1 = Yc + (yy-Yc)*math.cos(teta) - (xx-Xc)*math.sin(teta)
    
    pygame.draw.lines(screen, Color("black"),True, ((x1, y1),(xx1, yy1)), 2)
   
    x = counterx+100*k-7.6
    y = countery+10*k+6
    x1 = Xc + (x-Xc)*math.cos(teta) + (y-Yc)*math.sin(teta)
    y1 = Yc + (y-Yc)*math.cos(teta) - (x-Xc)*math.sin(teta)
    xx = counterx+80*k+6
    yy = countery+30*k-7.6
    xx1 = Xc + (xx-Xc)*math.cos(teta) + (yy-Yc)*math.sin(teta)
    yy1 = Yc + (yy-Yc)*math.cos(teta) - (xx-Xc)*math.sin(teta)
    
    pygame.draw.lines(screen, Color("black"),True, ((x1, y1),(xx1, yy1)), 2)
    
    

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
DISPLAY = (SCREEN_WIDTH,SCREEN_HEIGHT)		# задаем размеры окна
											 
pygame.init()	# иницилиализируем pygame
screen = pygame.display.set_mode(DISPLAY)	# создаем окно
pygame.display.set_caption('Бесподобная анимация')		# даем название окну

#основной цикл программы, где происходит рисование
done = False
clock = pygame.time.Clock()
bg = Surface(DISPLAY)	    # создаем Surface с разрамерами окна

                             

night_timer = 700
counter_sun = 0
countery_sun = 0
counterx_sun = 0
ang_sun = math.pi
ang_air = math.pi
counterx_cloud1 = SCREEN_WIDTH
countery_cloud1 = 60
counterx_cloud2 = SCREEN_WIDTH+60
countery_cloud2 = 120
counterx_cloud3 = SCREEN_WIDTH+500
countery_cloud3 = 150
counterx_aircraft = -200
countery_aircraft = 120
counterx_car = -300
countery_car = 600
teta_car = math.pi
bb1 = True
gr =0
bl =0
counter_star = 1
k_star = 0.05
while not done:
	
         
    # обработка завершения работы программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # выход из цикла

    screen.blit(bg, (0,0)) # холст в точке (0,0)

    # солнце и день
    if bb1:

        if gr <190:
            gr+=5
        if gr == 190:
            gr = 191
        if bl < 252:
            bl+=7
        if bl == 252:
            bl=255
        bg.fill(Color(0,gr,bl))
        counter_sun +=0.3
        counterx_sun = SCREEN_WIDTH//2 + 570* math.cos(ang_sun)
        countery_sun = 270 + 200 * math.sin(ang_sun)
        ang_sun+=0.005
        sun(screen,counter_sun,counterx_sun, countery_sun)
        bb = False
        if counterx_sun > SCREEN_WIDTH+50:
            bb = True
            gr = 191
            bl = 255
            night_timer = 700
            ang_sun = math.pi
    if bb:
        # звезды и ночь
        bb1 = False
        night_timer -=2

        if gr >1:
            gr-=5
        if gr == 1:
            gr = 0
        if bl > 0:
            bl-=5
        bg.fill(Color(0,gr,bl))
        if gr==bl == 0:
            counter_star+=k_star
            if counter_star > 1.5:
                counter_star = 1
                k_star = -0.05
            if counter_star < 0.5:
                counter_star = 1
                k_star = 0.05                    
            
            star(screen,counter_star,300,200)
            star(screen,counter_star,300,400)
            star(screen,counter_star,400,450)
            star(screen,counter_star,700,120)
            star(screen,counter_star,10,100)
            star(screen,counter_star,900,230)
        if night_timer<0:
            bb1 = True
            gr = 0
            bl = 0

        



        
        
    # облака
    counterx_cloud1-=1
    counterx_cloud2-=1
    counterx_cloud3-=1
    cloud(screen, counterx_cloud1, countery_cloud1)
    cloud(screen, counterx_cloud2, countery_cloud2)
    cloud(screen, counterx_cloud3, countery_cloud3)
    if counterx_cloud1 <-200:
        counterx_cloud1 = SCREEN_WIDTH
    if counterx_cloud2 <-200:
        counterx_cloud2 = SCREEN_WIDTH

    if counterx_cloud3 <-200:
        counterx_cloud3 = SCREEN_WIDTH
       
        
    # самолет     
    counterx_aircraft = SCREEN_WIDTH//2 + 750* math.cos(ang_air)
    countery_aircraft = 100 - 200 * math.sin(ang_air)
    ang_air+=0.008
    aircraft(screen,counterx_aircraft,countery_aircraft)
    if counterx_aircraft > SCREEN_WIDTH+60:
        ang_air = math.pi
    # дорога и машина   
    road(screen,SCREEN_WIDTH,SCREEN_HEIGHT-200)
    teta_car+=0.05
    counterx_car += 3 
    car(screen, counterx_car, countery_car, teta_car,bb1)
    if counterx_car > SCREEN_WIDTH+60:
        counterx_car = -300

    
    #отображаем все изменения на экране
    pygame.display.flip()
    clock.tick(60)


# завершаем работу pygame
pygame.quit()           
