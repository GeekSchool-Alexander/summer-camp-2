import pygame as pg

from VectorClass import Vec2d as vec
from settings import *


class Saw(pg.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.frames = (
		pg.image.load("./images/saw0.png"),
		pg.image.load("./images/saw1.png"),
		pg.image.load("./images/saw2.png"),
		pg.image.load("./images/saw3.png"),
		pg.image.load("./images/saw4.png"),
		pg.image.load("./images/saw5.png"),
		pg.image.load("./images/saw6.png"),
		pg.image.load("./images/saw7.png"))
		self.current_frame = 0
		self.last_update = pg.time.get_ticks()
		self.image = self.frames[self.current_frame]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	
	def update(self):
		self.animate()
	
	def animate(self):
		now = pg.time.get_ticks()
		if now - self.last_update >= SAW_ANIMATE_DELAY:
			self.last_update = now
			self.current_frame += 1
			if self.current_frame >= len(self.frames):
				self.current_frame = 0
			self.image = self.frames[self.current_frame]

class FlyingSaw(Saw):
	def __init__(self, x, y, direction, platforms):
		super().__init__(x, y)
		self.vel = self.generate_speed(direction)
		self.platforms = platforms
	
	def generate_speed(self, direct):
		if isinstance(direct, str):
			vel = vec(0, 0)
			if direct == "up":
				vel = vec(0, -SAW_SPEED)
			elif direct == "down":
				vel = vec(0, SAW_SPEED)
			elif direct == "left":
				vel = vec(-SAW_SPEED, 0)
			elif direct == "right":
				vel = vec(SAW_SPEED, 0)
			else:
				raise ValueError("Invalid direction")
			return vel
		else:
			raise TypeError("Direction must be str")
	
	def update(self):
		self.animate()
		self.collide_processing()
		self.rect.x += self.vel.x
		self.rect.y += self.vel.y
	
	def collide_processing(self):
		hits = pg.sprite.spritecollide(self, self.platforms, False)
		if hits:
			self.vel = -self.vel
