import pygame as pg

from platform import Platform
from player import Player
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
		
		self.player = Player(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
		self.all_sprites.add(self.player)
		
		p = Platform(800, 500)
		self.all_sprites.add(p)
		self.platforms.add(p)
		
		self.run()
		
	def main(self):
		while self.running:
			self.new()
	
	def __del__(self):
		pg.quit()
		

g = Game()
g.main()
