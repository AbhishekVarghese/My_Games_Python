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

while True :
	
