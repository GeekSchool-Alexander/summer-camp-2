import pygame as pg

import levels
from platform import Platform
from player import Player
from portal import Portal
from saw import Saw, FlyingSaw
from settings import *


class Game:
	def __init__(self):
		pg.init()
		pg.display.set_caption("GeekSchool Platformer")
		pg.display.set_icon(pg.image.load("./images/icon.jpg"))
		self.screen = pg.display.set_mode(WINDOW_SIZE)
		self.background = pg.image.load("./images/background.jpg")
		self.clock = pg.time.Clock()
		self.font = pg.font.SysFont("timesnewroman", 200)
		self.win_text = self.font.render("YOU WIN", 1, DARK_GREEN)
		self.player_won = False
		self.running = True
	
	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.playing = False
				self.running = False
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.playing = False
					self.running = False
	
	def update(self):
		self.all_sprites.update()
	
	def draw(self):
		self.screen.blit(self.background, (0, 0))
		self.all_sprites.draw(self.screen)
		if self.player_won:
			self.screen.blit(self.win_text, (75, 150))
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
		
		plts_conf, plr_conf, saw_conf, fl_saw_conf, prtl_conf = self.create_level(levels.level1)
		
		self.player = Player(*plr_conf, self)
		self.all_sprites.add(self.player)
		
		for plt in plts_conf:
			p = Platform(*plt)
			self.all_sprites.add(p)
			self.platforms.add(p)
		
		for saw in saw_conf:
			s = Saw(*saw)
			self.all_sprites.add(s)
			self.saws.add(s)
		
		for fl_saw in fl_saw_conf:
			s = FlyingSaw(*fl_saw, self.platforms)
			self.all_sprites.add(s)
			self.saws.add(s)
			
		self.portal = Portal(*prtl_conf)
		self.all_sprites.add(self.portal)

		self.run()

	def create_level(self, lvl):
		x = y = 0
		player_config = (0, 0)
		portal_config = (0, 0)
		platforms_config = []
		saws_config = []
		flying_saws_config = []
		for row in lvl:
			for cell in row:
				if cell == "-":
					platforms_config.append((x, y))
				if cell == "o":
					player_config = (x, y)
				if cell == "*":
					saws_config.append((x, y))
				if cell == "<":
					flying_saws_config.append((x, y, "left"))
				if cell == ">":
					flying_saws_config.append((x, y, "right"))
				if cell == "^":
					flying_saws_config.append((x, y, "up"))
				if cell == "v":
					flying_saws_config.append((x, y, "down"))
				if cell == "x":
					portal_config = (x, y)
				x += PLATFORM_WIDTH
			y += PLATFORM_HEIGHT
			x = 0
		return tuple(platforms_config), player_config, tuple(saws_config), tuple(flying_saws_config), portal_config
		
	def main(self):
		while self.running:
			self.new()
	
	def __del__(self):
		pg.quit()
		

g = Game()
g.main()
