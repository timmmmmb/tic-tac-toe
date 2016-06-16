import pygame, game, sys, math, box ,random

class Interface():
	def __init__(self):
		self.round = 0
		
		self.x = self.y = 0
		self.turn = 0 #0 player kreis 1 player kreuz
		self.boxes = []
		self.font = pygame.font.Font(None, 36)
		self.winner = 3 #0 player kreis 1 player kreuz 2 unentschieden 3 am spielen
		self.boxol = box.Box(10,50)
		self.boxom = box.Box(200,50)
		self.boxor = box.Box(390,50)
		
		self.boxml = box.Box(10,240)
		self.boxmm = box.Box(200,240)
		self.boxmr = box.Box(390,240)
		
		self.boxul = box.Box(10,430)
		self.boxum = box.Box(200,430)
		self.boxur = box.Box(390,430) 
		
		
		
		self.boxes.append(self.boxol)
		self.boxes.append(self.boxom)
		self.boxes.append(self.boxor)
		
		self.boxes.append(self.boxml)
		self.boxes.append(self.boxmm)
		self.boxes.append(self.boxmr)
		
		self.boxes.append(self.boxul)
		self.boxes.append(self.boxum)
		self.boxes.append(self.boxur)
		
	def update(self):
		mouserect = pygame.Rect(self.x, self.y, 5, 5)
		self.x = self.y = 0
		if self.turn == 0 and self.winner == 3:
			self.turntext =  self.font.render("Turn: Player Kreis",1,(255, 255, 255)) 
		elif self.turn == 1 and self.winner == 3:
			self.turntext =  self.font.render("Turn: Player Kreuz",1,(255, 255, 255))
		elif self.winner == 0:
			self.turntext =  self.font.render("Kreis gewinnt",1,(255, 255, 255))
		elif self.winner == 1:
			self.turntext =  self.font.render("Kreuz gewinnt",1,(255, 255, 255))
		elif self.winner == 2:	
			self.turntext =  self.font.render("Unentschieden",1,(255, 255, 255))
		for box in self.boxes:
			if box.status == 2 and mouserect.colliderect(box.rect) and self.winner == 3 and self.turn == 0:
				box.status = self.turn
				if self.turn == 0:
					self.turn = 1
				elif self.turn == 1:
					self.turn = 0 	
				
				self.round = self.round + 1
				break	
			elif self.turn == 1:
				self.botzug()
				self.round = self.round + 1	
				self.turn = 0 
				break	
				
		pressed_keys = pygame.key.get_pressed()
		if pressed_keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
		elif pressed_keys[pygame.K_SPACE]:
			self.restart()

		if self.boxul.status == 0 and self.boxum.status == 0 and self.boxur.status == 0 or self.boxml.status == 0 and self.boxmm.status == 0 and self.boxmr.status == 0 or self.boxol.status == 0 and self.boxom.status == 0 and self.boxor.status == 0 or self.boxol.status == 0 and self.boxml.status == 0 and self.boxul.status ==0 or self.boxom.status == 0 and self.boxmm.status == 0 and self.boxum.status ==0 or self.boxor.status == 0 and self.boxmr.status == 0 and self.boxur.status == 0 or self.boxol.status == 0 and self.boxmm.status == 0 and self.boxur.status == 0 or self.boxor.status == 0 and self.boxmm.status == 0 and self.boxul.status == 0:
			self.winner  = 0
		elif self.boxul.status == 1 and self.boxum.status == 1 and self.boxur.status == 1 or self.boxml.status == 1 and self.boxmm.status == 1 and self.boxmr.status == 1 or self.boxol.status == 1 and self.boxom.status == 1 and self.boxor.status == 1 or self.boxol.status == 1 and self.boxml.status == 1 and self.boxul.status ==1 or self.boxom.status == 1 and self.boxmm.status == 1 and self.boxum.status ==1 or self.boxor.status == 1 and self.boxmr.status == 1 and self.boxur.status == 1 or self.boxol.status == 1 and self.boxmm.status == 1 and self.boxur.status == 1 or self.boxor.status == 1 and self.boxmm.status == 1 and self.boxul.status == 1:
			self.winner  = 1
		elif self.round == 9:
			self.winner = 2
				
	def draw(self):	
		game.display.blit(self.turntext, pygame.Rect(180, 5, 20, 20))
		for box in self.boxes:
			box.draw()
			
	def restart(self):
		for box in self.boxes:
			box.status = 2
		self.winner = 3	
		self.round = 0
		
	def botzug(self):
		if self.winner == 3:	
				#wenn der bot 2 nebeneinander hat dann wird das dritte ausgefüllt
			if self.boxul.status == 1 and self.boxum.status == 1 and self.boxur.status == 2:
				self.boxur.status = 1
			elif 	self.boxul.status == 1 and self.boxur.status == 1 and self.boxum.status == 2:
				self.boxum.status = 1
			elif 	self.boxum.status == 1 and self.boxur.status == 1 and self.boxul.status == 2:
				self.boxul.status = 1	
				
			elif self.boxml.status == 1 and self.boxmm.status == 1 and self.boxmr.status == 2:
				self.boxmr.status = 1
			elif 	self.boxml.status == 1 and self.boxmr.status == 1 and self.boxmm.status == 2:
				self.boxmm.status = 1
			elif 	self.boxmm.status == 1 and self.boxmr.status == 1 and self.boxml.status == 2:
				self.boxml.status = 1	
				
			elif self.boxol.status == 1 and self.boxom.status == 1 and self.boxor.status == 2:
				self.boxor.status = 1
			elif 	self.boxol.status == 1 and self.boxor.status == 1 and self.boxom.status == 2:
				self.boxom.status = 1
			elif 	self.boxom.status == 1 and self.boxor.status == 1 and self.boxol.status == 2:
				self.boxol.status = 1
	
			elif self.boxol.status == 1 and self.boxml.status == 1 and self.boxul.status == 2:
				self.boxul.status = 1
			elif 	self.boxol.status == 1 and self.boxul.status == 1 and self.boxml.status == 2:
				self.boxml.status = 1
			elif 	self.boxul.status == 1 and self.boxml.status == 1 and self.boxol.status == 2:
				self.boxol.status = 1
			
			elif self.boxor.status == 1 and self.boxmr.status == 1 and self.boxur.status == 2:
				self.boxur.status = 1
			elif 	self.boxmr.status == 1 and self.boxur.status == 1 and self.boxor.status == 2:
				self.boxor.status = 1
			elif 	self.boxor.status == 1 and self.boxur.status == 1 and self.boxmr.status == 2:
				self.boxmr.status = 1
			
			elif self.boxmm.status == 1 and self.boxom.status == 1 and self.boxum.status == 2:
				self.boxum.status = 1
			elif 	self.boxum.status == 1 and self.boxmm.status == 1 and self.boxom.status == 2:
				self.boxom.status = 1
			elif 	self.boxom.status == 1 and self.boxum.status == 1 and self.boxmm.status == 2:
				self.boxmm.status = 1
				
			elif self.boxol.status == 1 and self.boxmm.status == 1 and self.boxur.status == 2:
				self.boxur.status = 1
			elif 	self.boxur.status == 1 and self.boxmm.status == 1 and self.boxol.status == 2:
				self.boxol.status = 1
			elif 	self.boxol.status == 1 and self.boxur.status == 1 and self.boxmm.status == 2:
				self.boxmm.status = 1
	
			elif self.boxor.status == 1 and self.boxmm.status == 1 and self.boxul.status == 2:
				self.boxul.status = 1
			elif 	self.boxul.status == 1 and self.boxmm.status == 1 and self.boxor.status == 2:
				self.boxor.status = 1
			elif 	self.boxul.status == 1 and self.boxor.status == 1 and self.boxmm.status == 2:
				self.boxmm.status = 1	
				#wenn der spieler 2 nebeneinander hat dann wird das dritte ausgefüllt
				
			elif self.boxul.status == 0 and self.boxum.status == 0 and self.boxur.status == 2:
				self.boxur.status = 1
			elif 	self.boxul.status == 0 and self.boxur.status == 0 and self.boxum.status == 2:
				self.boxum.status = 1
			elif 	self.boxum.status == 0 and self.boxur.status == 0 and self.boxul.status == 2:
				self.boxul.status = 1	
				
			elif self.boxml.status == 0 and self.boxmm.status == 0 and self.boxmr.status == 2:
				self.boxmr.status = 1
			elif 	self.boxml.status == 0 and self.boxmr.status == 0 and self.boxmm.status == 2:
				self.boxmm.status = 1
			elif 	self.boxmm.status == 0 and self.boxmr.status == 0 and self.boxml.status == 2:
				self.boxml.status = 1	
				
			elif self.boxol.status == 0 and self.boxom.status == 0 and self.boxor.status == 2:
				self.boxor.status = 1
			elif 	self.boxol.status == 0 and self.boxor.status == 0 and self.boxom.status == 2:
				self.boxom.status = 1
			elif 	self.boxom.status == 0 and self.boxor.status == 0 and self.boxol.status == 2:
				self.boxol.status = 1
	
			elif self.boxol.status == 0 and self.boxml.status == 0 and self.boxul.status == 2:
				self.boxul.status = 1
			elif 	self.boxol.status == 0 and self.boxul.status == 0 and self.boxml.status == 2:
				self.boxml.status = 1
			elif 	self.boxul.status == 0 and self.boxml.status == 0 and self.boxol.status == 2:
				self.boxol.status = 1
			
			elif self.boxor.status == 0 and self.boxmr.status == 0 and self.boxur.status == 2:
				self.boxur.status = 1
			elif 	self.boxor.status == 0 and self.boxur.status == 0 and self.boxmr.status == 2:
				self.boxmr.status = 1
			elif 	self.boxmr.status == 0 and self.boxur.status == 0 and self.boxor.status == 2:
				self.boxor.status = 1
			
			elif self.boxmm.status == 0 and self.boxom.status == 0 and self.boxum.status == 2:
				self.boxum.status = 1
			elif 	self.boxum.status == 0 and self.boxmm.status == 0 and self.boxom.status == 2:
				self.boxom.status = 1
			elif 	self.boxom.status == 0 and self.boxum.status == 0 and self.boxmm.status == 2:
				self.boxmm.status = 1
				
			elif self.boxol.status == 0 and self.boxmm.status == 0 and self.boxur.status == 2:
				self.boxur.status = 1
			elif 	self.boxur.status == 0 and self.boxmm.status == 0 and self.boxol.status == 2:
				self.boxol.status = 1
			elif 	self.boxol.status == 0 and self.boxur.status == 0 and self.boxmm.status == 2:
				self.boxmm.status = 1
	
			elif self.boxor.status == 0 and self.boxmm.status == 0 and self.boxul.status == 2:
				self.boxul.status = 1
			elif 	self.boxul.status == 0 and self.boxmm.status == 0 and self.boxor.status == 2:
				self.boxor.status = 1
			elif 	self.boxul.status == 0 and self.boxor.status == 0 and self.boxul.status == 2:
				self.boxmm.status = 1
				#wenn niergends 2 nebeneinander sind wird so fortgefahren
			elif self.boxmm.status == 2:
				self.boxmm.status = 1
			elif self.boxol.status == 2:
				self.boxol.status = 1
			elif self.boxor.status == 2:
				self.boxor.status = 1
			elif self.boxul.status == 2:
				self.boxul.status = 1
			elif self.boxur.status == 2:
				self.boxur.status = 1
			elif self.boxml.status == 2:
				self.boxml.status = 1
			elif self.boxmr.status == 2:
				self.boxmr.status = 1
			elif self.boxom.status == 2:
				self.boxom.status = 1	
			elif self.boxum.status == 2:
				self.boxum.status = 1
					
			
		
		
		
		
		
		