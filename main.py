import pygame, game, sys
#Autor: Tim Frey
#Title: Tic-Tac-Toe
#Date: 25. 01. 2016
#Version 1.0


# Game initialization hier werden alle objekte erstellt und alle wichtigen variablen erstellt
game.init()
clock = pygame.time.Clock()


# Gameloop
#veraendert die x und y kordinaten des interface objekts
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			game.interface.x, game.interface.y = event.pos		
		game.update()
		game.draw()


	pygame.display.flip()

	clock.tick(30)