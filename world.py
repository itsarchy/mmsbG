import pygame

from content import *
from world import *
from tile import *
from entity import *
from settings import *

pygame.init()

class World:
	def __init__(self):
		self.level_map = []
	def loadMap(self, MAP_URL):
		self.level_map = []
		with open(MAP_URL, "r") as f:
			level_str = []
			for s in f.read():
				if s == "0":
					level_str.append(0)
				elif s == "1":
					level_str.append(1)
				elif s == "2":
					level_str.append(2)
				elif s == "\\":
					self.level_map.append(level_str)
					level_str = []
	def render(self):
		
		