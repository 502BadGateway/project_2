#!/usr/bin/python

import pygame
from pygame.locals import *

def main():
	robotScore = "10"
	robotScore2 = "11"
	pygame.init()
	screen = pygame.display.set_mode((640, 480))
	pygame.display.set_caption('Basic Pygame program')

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))

	font = pygame.font.Font(None, 36)
	text = font.render(robotScore, 1, (10, 10, 10))
	textpos = pygame.Rect(600,10,0,0)
	background.blit(text, textpos)

	text2 = font.render(robotScore2, 1, (10, 10, 10))
	textpos2 = pygame.Rect(600,30,0,0)
	background.blit(text2, textpos2)

	screen.blit(background, (0, 0))
	pygame.display.flip()

	# Event loop
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

		screen.blit(background, (0, 0))
		pygame.display.flip()


if __name__ == '__main__': main()