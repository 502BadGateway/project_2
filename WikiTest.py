import wikipedia
import sys
reload(sys)
LandInfo = wikipedia.summary("Taj Mahal", sentences = 2)
sys.setdefaultencoding('utf-8')
print LandInfo

import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Test text output")
myfont = pygame.font.SysFont("Comic Sans MS", 15)
label = myfont.render(LandInfo, 1, (250,250,250))
screen.blit(label, (100, 100))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit