import pygame as pg

from VectorClass import Vec2d as vec
from settings import *


class Player(pg.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pg.Surface(PLAYER_SIZE)
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)
		self.pos = vec(x, y)
	
	def update(self):
		self.acc = vec(0, 0)
		
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			self.acc.x = -PLAYER_ACC
		elif keys[pg.K_RIGHT]:
			self.acc.x = PLAYER_ACC
		
		self.acc -= self.vel * PLAYER_FRICTION
		self.vel += self.acc  # v = v0 + a*t
		self.pos += self.vel + self.acc/2  # x = x0 + v + a/2
		self.rect.center = self.pos
		
		if self.left < 0:
			self.left = 0
		elif self.right > WINDOW_WIDTH:
			self.right = WINDOW_WIDTH
		
		if self.top < 0:
			self.top = 0
		elif self.bottom > WINDOW_HEIGHT:
			self.bottom = WINDOW_HEIGHT

	@property
	def right(self):
		return self.pos.x + PLAYER_WIDTH/2
	
	@right.setter
	def right(self, x):
		self.pos.x = x - PLAYER_WIDTH/2
	
	@property
	def left(self):
		return self.pos.x - PLAYER_WIDTH/2
	
	@left.setter
	def left(self, x):
		self.pos.x = x + PLAYER_WIDTH/2
	
	@property
	def top(self):
		return self.pos.y - PLAYER_HEIGHT/2
	
	@top.setter
	def top(self, y):
		self.pos.y = y + PLAYER_HEIGHT/2
	
	@property
	def bottom(self):
		return self.pos.y + PLAYER_HEIGHT/2
	
	@bottom.setter
	def bottom(self, y):
		self.pos.y = y - PLAYER_HEIGHT/2