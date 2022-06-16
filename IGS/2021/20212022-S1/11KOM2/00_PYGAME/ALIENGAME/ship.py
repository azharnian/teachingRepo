import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

	def __init__(self, AlienGame):
		super().__init__()
		
		self.screen = AlienGame.screen
		self.settings = AlienGame.settings
		self.screen_rect = AlienGame.screen.get_rect()

		self.image = pygame.image.load('assets/ship.bmp')
		self.rect = self.image.get_rect()
		self.center_ship()

		#movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def center_ship(self):
		self.rect.midbottom = self.screen_rect.midbottom

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.x += self.settings.SHIP_SPEED

		if self.moving_left and self.rect.left > 0:
			self.rect.x -= self.settings.SHIP_SPEED

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.y += self.settings.SHIP_SPEED

		if self.moving_up and self.rect.top > 0:
			self.rect.y -= self.settings.SHIP_SPEED


	def blitme(self): #show
		self.screen.blit(self.image, self.rect)