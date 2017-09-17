import pygame

from pygame.sprite import Group, groupcollide

pygame.init()

screen_size = (1000,800)
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("FIRST FANTASY.")
background_image = pygame.image.load("ffbackgroundsmall.png")

# find music later
# pygame.mixer.init()
# pygame.mixer.music.load()
# pygame.mixer.music.play()

game_on = True

while game_on: 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_on = False

		
	pygame_screen.blit(background_image, [0,0])

	pygame.display.flip()

