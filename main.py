import pygame as pg
from settings import *


class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode(WINDOW_SIZE)
		self.clock = pg.time.Clock()
		
	def __del__(self):
		pg.quit()
		

g = Game()
