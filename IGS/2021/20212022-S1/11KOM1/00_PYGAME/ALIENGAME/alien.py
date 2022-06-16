import pygame
from pygame.sprite import Sprite

class Alien(Sprite):


	def __init__(self, AlienGame):
		super().__init__()
		self.screen = AlienGame.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = AlienGame.settings

		self.image = pygame.image.load("assets/alien.bmp")
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image, (self.rect.width//2, self.rect.height//2))
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

	def update(self):
		self.rect.x += self.settings.ALIEN_SPEED


	def check_edges(self):
		if (self.rect.right >= self.screen_rect.right) or (self.rect.left <= 0):
			return True