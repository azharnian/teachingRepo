import pygame

class Platform(pygame.sprite.Sprite):

	def __init__(self, FlappyBird):
		super().__init__()
		self.my_settings = FlappyBird.my_settings
		self.my_screen = FlappyBird.my_screen
		self.my_statistics = FlappyBird.my_statistics

		self.image = pygame.image.load(self.my_settings.PLATFORM_IMG) #sprite -> image, rect
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.my_screen.screen_rect.midbottom

	def move(self):
		if not self.my_statistics.paused:
			if self.rect.right <= self.my_screen.screen_rect.left:
				self.rect.left = self.my_screen.screen_rect.right
			self.rect.x -= self.my_settings.PLATFORM_SPEED

