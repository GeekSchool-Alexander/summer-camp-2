import pygame as pg

from VectorClass import Vec2d as vec
from settings import *


class Player(pg.sprite.Sprite):
	def __init__(self, x, y, platforms):
		super().__init__()
		self.image = pg.image.load("./images/ball.png")
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)
		self.pos = vec(x, y)
		self.platforms = platforms
		self.on_ground = False
	
	def update(self):
		
		self.acc = vec(0, PLAYER_GRAVITY)
		
		self.keydown_processing()
		
		self.acc -= self.vel * PLAYER_FRICTION
		self.vel += self.acc  # v = v0 + a*t
		self.pos += self.vel + self.acc/2  # x = x0 + v + a/2
		
		self.wall_processing()
		self.collide_processing()
		
		self.rect.center = self.pos
	
	def keydown_processing(self):
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			self.acc.x = -PLAYER_ACC
		elif keys[pg.K_RIGHT]:
			self.acc.x = PLAYER_ACC
		if keys[pg.K_UP]:
			self.jump()
			
	def jump(self):
		if self.on_ground:
			self.vel.y = -PLAYER_JUMP
		
	def collide_processing(self):
		self.on_ground = False
		hits = pg.sprite.spritecollide(self, self.platforms, False)
		if hits:
			platform = hits[0]
			
			collides = set()
			for side, plat_rect in platform.lines.items():
				if self.rect.colliderect(plat_rect):
					collides.add(side)
			
			if "top" in collides:
				self.vel.y = 0
				self.bottom = platform.top
				self.on_ground = True
			elif "bottom" in collides:
				self.vel.y = 0
				self.top = platform.bottom
			elif "left" in collides:
				self.vel.x = 0
				self.right = platform.left
			elif "right" in collides:
				self.vel.x = 0
				self.left = platform.right
			
				
			
			

	def wall_processing(self):
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
