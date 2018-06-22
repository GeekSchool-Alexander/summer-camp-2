import pygame as pg

from settings import *


class Platform(pg.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pg.image.load("./images/brick.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.lines = self.create_lines()
	
	def create_lines(self):
		lines = {"left" : pg.Rect(self.rect.x+PLATFORM_EMPTY_CORNER, self.rect.y, PLATFORM_WIDTH - PLATFORM_EMPTY_CORNER*2, 1)}
		return lines