import pygame, interface

def init():
	pygame.init()
	global display
	display = pygame.display.set_mode((580, 620))
	
	#das Interface objekt wird erstellt
	global interface
	interface = interface.Interface()

def draw():
	global display
	display.fill((0,0,0))
	global interface
	interface.draw()
	
def update():
	global interface
	interface.update()