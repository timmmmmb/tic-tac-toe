import pygame, game

class Box():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.status = 2 #2 leer 0 player kreis 1 player kreuz
		self.rect = pygame.Rect(self.x, self.y, 180, 180)
		self.imageleer = pygame.image.load('images/leer.png').convert_alpha()
		self.imagekreuz = pygame.image.load('images/kreuz.png').convert_alpha()
		self.imagekreis = pygame.image.load('images/kreis.png').convert_alpha()
		
	
	def draw(self):	
		if self.status == 2:
			game.display.blit(self.imageleer, self.rect)
		elif self.status == 1:
			game.display.blit(self.imagekreuz, self.rect)
		elif self.status == 0:
			game.display.blit(self.imagekreis, self.rect)