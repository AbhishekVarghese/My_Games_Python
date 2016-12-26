import pygame,random,sys,time
from pygame.locals import *
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,200,0)
BLUE = (100,100,255)
AQUA = (0,180,250)

resolution = [1300,600]

fontObj = pygame.font.Font('freesansbold.ttf', 32)


clock = pygame.time.Clock()
FPS = 200
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Tron")

class Player(object) :
    def __init__(self,x,y,color,name) :
        self.x = x
        self.y = y
        self.color = color
        self.increment = 1
        self.length = 5
        self.boost = 3
        self.boost_using = False
        self.gameover = False
        self.doing = 0 # 1 :up. 2 :down. 3 Left 4 right
        self.score =0
        self.sttime = 0
        self.name = name

p2 = Player(10,resolution[1]-10,BLUE,"Purple")
p1 = Player(resolution[0]-10,resolution[1]-10,GREEN,"Green")



def draw_screen(n = 0 ) :
    if n==0 :
        screen.fill(BLACK)
level = 0
draw_screen(level)

while True :
    
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if not p1.gameover :
                if event.key == K_LEFT and not p1.doing == 4:
                    if p1.doing == 3 and p1.boost > 0 and not p1.boost_using:
                        p1.increment = 5
                        p1.boost -= 1
                        p1.sttime = time.time()
                        p1.boost_using = True
                    p1.doing = 3
                if event.key == K_RIGHT and not p1.doing == 3:
                    if p1.doing == 4 and p1.boost > 0 and not p1.boost_using:
                        p1.increment = 5
                        p1.boost -= 1
                        p1.sttime = time.time()
                        p1.boost_using = True
                    p1.doing = 4
                if event.key == K_UP and not p1.doing == 2:
                    if p1.doing == 1 and p1.boost > 0 and not p1.boost_using:
                        p1.increment = 5
                        p1.boost -= 1
                        p1.sttime = time.time()
                        p1.boost_using = True
                    p1.doing = 1
                if event.key == K_DOWN and not p1.doing == 1:
                    if p1.doing == 2 and p1.boost > 0 and not p1.boost_using:
                        p1.increment = 5
                        p1.boost -= 1
                        p1.sttime = time.time()
                        p1.boost_using = True
                    p1.doing = 2

            if not p2.gameover :
                if event.key == K_a and not p2.doing == 4:
                    if p2.doing == 3 and p2.boost > 0 and not p2.boost_using:
                        p2.increment = 5
                        p2.boost -= 1
                        p2.sttime = time.time()
                        p2.boost_using = True
                    p2.doing = 3
                if event.key == K_d and not p2.doing == 3 :
                    if p2.doing == 4 and p2.boost > 0 and not p2.boost_using:
                        p2.increment = 5
                        p2.boost -= 1
                        p2.sttime = time.time()
                        p2.boost_using = True
                    p2.doing = 4
                if event.key == K_w and not p2.doing == 2:
                    if p2.doing == 1 and p2.boost > 0 and not p2.boost_using:
                        p2.increment = 5
                        p2.boost -= 1
                        p2.sttime = time.time()
                        p2.boost_using = True
                    p2.doing = 1
                if event.key == K_s and not p2.doing == 1:
                    if p2.doing == 2 and p2.boost > 0 and not p2.boost_using:
                        p2.increment = 5
                        p2.boost -= 1
                        p2.sttime = time.time()
                        p2.boost_using = True
                    p2.doing = 2
    
    for i in [p1,p2] :
        # -----------------------------------
        if i.gameover :
            for r in range (100) :
                pygame.draw.circle(screen,i.color,(i.x,i.y),r)
                pygame.display.update()
            for r in range (100) :
                pygame.draw.circle(screen,BLACK,(i.x,i.y),r)
                pygame.display.update()
            
            temp = True
            g = [p1,p2]
            g.remove(i)
            g = g[0]
            g.score += 1
            a= g.name + "  " + random.choice(['Bashed','Dashed','Squished','Smashed','Fried']) + " " +i.name + " " +random.choice(['to pulp','to peices','out of %s juices. And now he is colorless!!'%(str(i.name)),'to bits','brains out of %s tron'%(str(i.name))])
            tSO = fontObj.render(a, True, g.color,BLACK)
            tRO = tSO.get_rect()
            tRO.center = (resolution[0]/2, resolution[1]/2)
            tSO1 = fontObj.render("Scores : Purple - " + str(p2.score)+ ";  Green - " + str(p1.score), True, AQUA,BLACK)
            tRO1 = tSO1.get_rect()
            tRO1.center = (resolution[0]/2, resolution[1]/2+50)
            
            while temp :
                screen.blit(tSO,tRO)
                screen.blit(tSO1,tRO1)
                for event in pygame.event.get():
                    if event.type == QUIT :
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                       if event.key == K_r :
                            p2.x = 10
                            p2.y = resolution[1]-10
                            p1.gameover = False
                            p2.gameover = False
                            p1.increment = 2
                            p2.increment = 2
                            p1.doing = 0
                            p2.doing = 0
                            p1.boost = 3
                            p2.boost = 3
                            p1.x = resolution[0]-10
                            p1.y = resolution[1]-10
                            temp = False
                            draw_screen(level)
                            break
                pygame.display.update()
            del temp
            break
        # -----------------------------------------------------------
            
        '''if not i.gameover :
            if i.doing == 1 :
                if i.y - i.increment <= 0 or screen.get_at((i.x,i.y - i.increment)) != BLACK :
                    i.gameover = True
                    break
                i.y -= i.increment
            if i.doing == 2 :
                if i.y + i.increment + i.length >= resolution[1] or screen.get_at((i.x,i.y + i.increment + i.length)) != BLACK :
                    i.gameover = True
                    break
                i.y += i.increment
            if i.doing == 3 :
                if i.x - i.increment <= 0 or screen.get_at((i.x - i.increment,i.y)) != BLACK :
                    i.gameover = True
                    break
                i.x -= i.increment
            if i.doing == 4 :
                if i.x + i.increment + i.length >= resolution[0] or screen.get_at((i.x + i.increment + i.length,i.y)) != BLACK :
                    i.gameover = True
                    break
                i.x += i.increment'''
        if not i.gameover :
            if i.doing == 1 :
                
                if i.y - i.increment <= 0 :
                    i.y = resolution[1] - 10
                elif screen.get_at((i.x,i.y - i.increment)) != BLACK :
                    i.gameover = True
                    break
                i.y -= i.increment
            if i.doing == 2 :
                if  i.y + i.increment + i.length >= resolution[1]:
                    i.y = 0
                elif  screen.get_at((i.x,i.y + i.increment + i.length)) != BLACK :
                    i.gameover = True
                    break
                i.y += i.increment
            if i.doing == 3 :
                
                if i.x - i.increment <= 0 :
                    i.x = resolution[0] - 10
                elif  screen.get_at((i.x - i.increment,i.y)) != BLACK :
                    i.gameover = True
                    break
                i.x -= i.increment
            if i.doing == 4 :
                
                if i.x + i.increment + i.length >= resolution[0] :
                    i.x = 0
                elif screen.get_at((i.x + i.increment + i.length,i.y)) != BLACK :
                    i.gameover = True
                    break
                i.x += i.increment
            
            
            
        # ----------------------------------------------------------------
        if i.boost_using and time.time() - i.sttime > 1 :
            i.boost_using = False
            i.increment =  2

    
    pygame.draw.rect(screen,p1.color,(p1.x,p1.y,p1.length,p1.length))
    pygame.draw.rect(screen,p2.color,(p2.x,p2.y,p2.length,p2.length))
    
    pygame.display.update()
    clock.tick(FPS)
                
                
            








    
