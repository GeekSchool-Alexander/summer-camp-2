import time

import pygame as pg

from VectorClass import Vec2d as vec
from settings import *


class Player(pg.sprite.Sprite):
	def __init__(self, x, y, game):
		super().__init__()
		self.frames = (pg.image.load("./images/ball0.png"),
		               pg.image.load("./images/ball1.png"),
		               pg.image.load("./images/ball2.png"),
		               pg.image.load("./images/ball3.png"),
		               pg.image.load("./images/ball4.png"),
		               pg.image.load("./images/ball5.png"),
		               pg.image.load("./images/ball6.png"),
		               pg.image.load("./images/ball7.png"))
		self.current_frame = 0
		self.last_update = pg.time.get_ticks()
		self.image = self.frames[self.current_frame]
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.vel = vec(0, 0)
		self.acc = vec(0, 0)
		self.pos = vec(x, y)
		self.game = game
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
		
		self.animate()
		
	def animate(self):
		now = pg.time.get_ticks()
		if now - self.last_update >= PLAYER_ANIMATE_DELAY:
			self.last_update = now
			if int(self.vel.x) > 0:
				self.current_frame += 1
				if self.current_frame >= len(self.frames):
					self.current_frame = 0
			elif int(self.vel.x) < 0:
				self.current_frame -= 1
				if self.current_frame < 0:
					self.current_frame = len(self.frames)-1
			self.image = self.frames[self.current_frame]
			
	def keydown_processing(self):
		keys = pg.key.get_pressed()
		if keys[pg.K_a]:
			self.acc.x = -PLAYER_ACC
		elif keys[pg.K_d]:
			self.acc.x = PLAYER_ACC
		if keys[pg.K_w]:
			self.jump()
			
	def jump(self):
		if self.on_ground:
			self.acc.y = -PLAYER_JUMP
		
	def collide_processing(self):
		# collide with platforms
		self.on_ground = False
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		if hits:
			collides = dict()
			for platform in hits:
				for side, plat_rect in platform.lines.items():
					if self.rect.colliderect(plat_rect):
						collides[side] = plat_rect
			
			if "top" in collides:
				self.vel.y = 0
				self.bottom = collides["top"].top
				self.on_ground = True
			elif "bottom" in collides:
				self.vel.y = 0
				self.top = collides["bottom"].bottom
			elif "left" in collides:
				self.vel.x = 0
				self.right = collides["left"].left
			elif "right" in collides:
				self.vel.x = 0
				self.left = collides["right"].right
				
		# collide with saws
		hits = pg.sprite.spritecollide(self, self.game.saws, False)
		if hits:
			time.sleep(1)
			self.game.playing = False
			
		# collide with portal
		hits = self.rect.colliderect(self.game.portal.rect)
		if hits:
			self.game.player_won = True
			pg.event.post(pg.event.Event(pg.QUIT))

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
