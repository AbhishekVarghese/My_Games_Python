import pygame,random,sys,time
from pygame.locals import *
pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,200,0)
BLUE = (100,100,255)
AQUA = (0,180,250)

resolution = [1250,450]

fontObj = pygame.font.Font('freesansbold.ttf', 30)

clock = pygame.time.Clock()
FPS = 10000
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Winx")


pygame.mixer.init()
pygame.mixer.music.load("factor_7.mp3")
pygame.mixer.music.play(-1)

class Rectangle():
	def __init__(self,length,width,color):
		self.color = color
		self.length=length
		self.width = width
	

def game_1(time_net) :
	time_start = 0
	n=0
	score=0
	increment =""
	correct = -1
	
	colors =[WHITE,BLUE,RED,AQUA,GREEN]
	position = [K_a,K_s,K_d,K_j,K_k]
	current_pos = random.choice(position)
	error_rect = (resolution[0]/5+10,resolution[1]/3+10,RED)
	correct_rect = (resolution[0]/5+10,resolution[1]/3+10,GREEN)
	while True :
		if (time.time() - time_start) > time_net :
				n=n+1
				current_pos = random.choice(position)
				current_rect = Rectangle(resolution[0]/5,resolution[1]/3,random.choice(colors))
				time_start = time.time()
		if (time.time() - time_start)>0.1 or correct == -1 :
			screen.fill(BLACK)
			if increment != "" :
				increment = ""
				correct = -1
		elif correct :
			screen.fill(GREEN)
		else:
			screen.fill(RED)
		tSO = fontObj.render(str(score)+str(increment), True,WHITE,BLACK)
		tRO = tSO.get_rect()
		tRO.center = (resolution[0]/2,100)
		
			
				
			
		for event in pygame.event.get():
		    if event.type == QUIT :
		        pygame.quit()
		        sys.exit()
		    if event.type == KEYDOWN :
		    	
		    	if event.key == current_pos :
		    		current_rect.color = BLACK
		    		score+=10
		    		correct = True
		    		increment = "(+10)"
		    		time_start-=time_net
		    	else :
		    		current_rect.color = BLACK
		    		score-=5
		    		increment = "(-5)"
		    		correct = False
		    		time_start-=time_net
    	
		
		pygame.draw.rect(screen,current_rect.color,(resolution[0]*position.index(current_pos)/5,resolution[1]/3,current_rect.length,current_rect.width))
		screen.blit(tSO,tRO)
		pygame.display.update()
		clock.tick(FPS)
		
game_1(0.75)
