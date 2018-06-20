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
		
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > WINDOW_WIDTH:
			self.rect.right = WINDOW_WIDTH
		
		if self.rect.top < 0:
			self.rect.top = 0
		elif self.rect.bottom > WINDOW_HEIGHT:
			self.rect.bottom = WINDOW_HEIGHT
