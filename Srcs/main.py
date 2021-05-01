import pygame
import random

pygame.init()

_sfondo_ = pygame.image.load('immagini/sfondo.png')
_bird_	= pygame.image.load('immagini/uccello.png')
_ground_ = pygame.image.load('immagini/base.png')
_gameover_ = pygame.image.load('immagini/gameover.png')
_pipedwn_ = pygame.image.load('immagini/tubo.png')
_pipeup_ = pygame.transform.flip(_pipedwn_, False, True)

WIN	= pygame.display.set_mode((288, 512))
pygame.display.set_caption("Flappy Bird!")
loop = True
while loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False
	WIN.fill((200, 0, 0))
	pygame.display.flip()
pygame.quit()
