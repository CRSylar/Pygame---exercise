import pygame

pygame.init()
loop = True
WIN = pygame.display.set_mode ((500, 500))
pygame.display.set_caption("Hello World!")
while loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False
	WIN.fill((200, 0, 0))
	pygame.display.flip()
pygame.quit()
