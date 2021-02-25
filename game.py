import pygame

from content import *
from world import *
from tile import *
from entity import *
from settings import *

pygame.init()

class Game:
	def __init__(self):
		self.screen_surface = pygame.display.set_mode(SCREEN_SIZE)
		self.run = True
		self.exit_attemp = False
		self.game_state = 0
		self.world = World()
		self.world.loadMap("map")
	
	def tick(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.exit_attemp = True
		if self.game_state == 0:
			pass
	
	def notEnded(self):
		return self.run