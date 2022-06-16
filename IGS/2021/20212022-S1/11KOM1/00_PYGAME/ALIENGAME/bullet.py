import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

	def __init__(self, AlienGame):

		super().__init__()
		self.screen = AlienGame.screen
		self.settings = AlienGame.settings
		self.ship = AlienGame.ship

		self.rect = pygame.Rect(0, 0, self.settings.BULLET_WIDTH, self.settings.BULLET_HEIGHT)
		self.rect.midtop = self.ship.rect.midtop

	def update(self):
		self.rect.y -= self.settings.BULLET_SPEED

	def draw(self):
		pygame.draw.rect(self.screen, self.settings.BULLET_COLOR, self.rect)
