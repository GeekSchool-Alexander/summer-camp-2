import pygame as pg

from settings import *


class Player(pg.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pg.Surface(PLAYER_SIZE)
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
