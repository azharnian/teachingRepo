import pygame

class Label:

	def __init__(self, FlappyBird, text):
		self.my_settings = FlappyBird.my_settings
		self.my_screen = FlappyBird.my_screen
		self.text = text
		self.font = pygame.font.Font(self.my_settings.LABEL_FONT, self.my_settings.LABEL_FONT_SIZE)
		self.text_image = self.font.render(self.text, True, self.my_settings.LABEL_FONT_COLOR)

		self.text_image_rect = self.text_image.get_rect()


	def blit(self):
		self.my_screen.screen.blit(self.text_image, self.text_image_rect)