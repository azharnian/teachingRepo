import pygame

class ScoreBoard:

	def __init__(self, FlappyBird):
		self.my_settings = FlappyBird.my_settings
		self.my_statistics = FlappyBird.my_statistics
		self.my_screen = FlappyBird.my_screen

		self.update_score_image()
		self.update_high_score_image()


	def update_score_image(self):
		self.score_image_font = pygame.font.Font(self.my_settings.FONT, self.my_settings.FONT_SIZE)
		self.score_image = self.score_image_font.render(str(self.my_statistics.score), True, self.my_settings.FONT_COLOR)

		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.centerx = self.my_screen.screen_rect.centerx
		self.score_image_rect.y += self.my_settings.SCREEN_WIDTH // 3

	def update_high_score_image(self):
		self.high_score_image_font = pygame.font.Font(self.my_settings.FONT, self.my_settings.FONT_SIZE-25)
		self.high_score_image = self.high_score_image_font.render("High: "+str(self.my_statistics.high_score), True, self.my_settings.FONT_COLOR)

		self.high_score_image_rect = self.high_score_image.get_rect()
		self.high_score_image_rect.topleft = self.my_screen.screen_rect.topleft
		self.high_score_image_rect.x += 20
		self.high_score_image_rect.y += 15

	def blit(self):
		self.my_screen.screen.blit(self.score_image, self.score_image_rect)
		self.my_screen.screen.blit(self.high_score_image, self.high_score_image_rect)

