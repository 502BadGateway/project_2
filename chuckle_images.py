import pygame #this imports pygames 
import sys 

from pygame.locals import* #this allows us to import pygame features 
robotpaul = pygame.image.load('chuckle-1.png') #this is a pygame feature which allows us to load images 
robotbarry = pygame.image.load ('chuckle-2.png')



white = (255, 255, 255) #pygame uses RGB for colours 
w = 640 
h = 480
screen = pygame.display.set_mode((w, h)) #this displays the game screen 



while True: #we placed it into loop so the image will continue to show 
    screen.blit(robotpaul,(0,0)) #this is needed as it displays everything into the screen  
    screen.blit(robotbarry,(450,0))

    pygame.display.flip() #This is neeed to have everything drawn in. 





