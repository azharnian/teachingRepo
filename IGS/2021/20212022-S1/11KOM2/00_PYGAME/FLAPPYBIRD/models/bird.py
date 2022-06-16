import pygame

class Bird:

	def __init__(self, FlappyBird):

		self.my_settings = FlappyBird.my_settings
		self.my_screen = FlappyBird.my_screen
		self.my_statistics = FlappyBird.my_statistics
		self.image = pygame.image.load(self.my_settings.BIRD_IMG)
		self.rect = self.image.get_rect()

		self.reposition()

		self.fly = False

		self.passing_pipe = False

	def reposition(self):
		self.rect.midleft = self.my_screen.screen_rect.midleft
		self.rect.x += 50


	def blit(self):
		self.my_screen.screen.blit(self.image, self.rect)


	def flying(self):
		if not self.my_statistics.paused:
			if self.fly:
				#self.image = pygame.transform.rotate(self.image, 90)
				self.rect.y -= self.my_settings.BIRD_FLY_SPEED
			else:
				self.rect.y += self.my_settings.BIRD_FALL_SPEED