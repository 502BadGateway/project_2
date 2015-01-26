import pygame 
import time
pygame.init() #initiates pygame

white = (255, 64, 64) #this is the colour, to be used later
w = 640 #the width of the dispaly varibale
h = 480 #the height of the display variable
screen = pygame.display.set_mode((w, h)) #creates the the dispay
screen.fill((white)) 

song = pygame.mixer.Sound('backgroundMusic.ogg') #creates an instants of the music
song.play() plays the music
while 1:
    for x in range(0,10000000):
        print x

    pygame.quit()
