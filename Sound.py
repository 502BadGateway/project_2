import pygame
import time
pygame.init()

white = (255, 64, 64)
w = 640
h = 480
screen = pygame.display.set_mode((w, h))
screen.fill((white))

song = pygame.mixer.Sound('backgroundMusic.ogg')
song.play()
while 1:
    for x in range(0,10000000):
        print x

    pygame.quit()
