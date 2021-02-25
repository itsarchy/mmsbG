import pygame
from game import *

pygame.init()

game = Game()

while game.notEnded():
	game.tick()

pygame.quit()
exit()