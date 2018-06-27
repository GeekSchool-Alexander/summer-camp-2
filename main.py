import pygame as pg

import levels
from platform import Platform
from player import Player
from saw import Saw, FlyingSaw
from settings import *


class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode(WINDOW_SIZE)
		self.clock = pg.time.Clock()
		self.running = True
	
	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.playing = False
				self.running = False
	
	def update(self):
		self.all_sprites.update()
	
	def draw(self):
		self.screen.fill(WHITE)
		self.all_sprites.draw(self.screen)
		pg.display.flip()
	
	def run(self):
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()
			
	def new(self):
		self.all_sprites = pg.sprite.Group()
		self.platforms = pg.sprite.Group()
		self.saws = pg.sprite.Group()
		
		plts_conf, plr_conf, saw_conf = self.create_level(levels.level1)
		
		self.player = Player(*plr_conf, self.platforms)
		self.all_sprites.add(self.player)
		
		for plt in plts_conf:
			p = Platform(*plt)
			self.all_sprites.add(p)
			self.platforms.add(p)
		
		for saw in saw_conf:
			s = Saw(*saw)
			self.all_sprites.add(s)
			self.saws.add(s)
		
		# TODO: flying saw generator
		s = FlyingSaw(0, 40, "right")
		self.all_sprites.add(s)
		self.saws.add(s)

		self.run()

	def create_level(self, lvl):
		x = y = 0
		player_config = (0, 0)
		platforms_config = []
		saws_config = []
		for row in lvl:
			for cell in row:
				if cell == "-":
					platforms_config.append((x, y))
				if cell == "o":
					player_config = (x, y)
				if cell == "*":
					saws_config.append((x, y))
				x += PLATFORM_WIDTH
			y += PLATFORM_HEIGHT
			x = 0
		return tuple(platforms_config), player_config, tuple(saws_config)
		
	def main(self):
		while self.running:
			self.new()
	
	def __del__(self):
		pg.quit()
		

g = Game()
g.main()
