import pygame

class Screen:

	def __init__(self, FlappyBird):
		self.settings = FlappyBird.my_settings
		self.my_statistics = FlappyBird.my_statistics
		self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH,self.settings.SCREEN_HEIGHT))
		self.screen_rect = self.screen.get_rect()

		self.bg_color = (0,0,0)
		self.bg_screen = pygame.image.load(self.settings.BG_SCREEN)
		self.bg_screen = pygame.transform.scale(self.bg_screen, (self.settings.SCREEN_WIDTH,self.settings.SCREEN_HEIGHT))


	def show(self):
		if not self.my_statistics.pre_game:
			self.screen.blit(self.bg_screen, (0,0))
		else:
			self.screen.fill(self.bg_color)


