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
		lines = {"top" : pg.Rect(self.rect.left+PLATFORM_EMPTY_CORNER, self.rect.top, PLATFORM_WIDTH - PLATFORM_EMPTY_CORNER*2, 1),
		         "bottom" : pg.Rect(self.rect.left+PLATFORM_EMPTY_CORNER, self.rect.bottom, PLATFORM_WIDTH - PLATFORM_EMPTY_CORNER*2, 1),
		         "left" : pg.Rect(self.rect.left, self.rect.top+PLATFORM_EMPTY_CORNER, 1, PLATFORM_HEIGHT-PLATFORM_EMPTY_CORNER*2),
		         "right" : pg.Rect(self.rect.right, self.rect.top+PLATFORM_EMPTY_CORNER, 1, PLATFORM_HEIGHT-PLATFORM_EMPTY_CORNER*2)}
		return lines
	
	@property
	def right(self):
		return self.rect.right
	
	@property
	def left(self):
		return self.rect.left
	
	@property
	def top(self):
		return self.rect.top
	
	@property
	def bottom(self):
		return self.rect.bottom
