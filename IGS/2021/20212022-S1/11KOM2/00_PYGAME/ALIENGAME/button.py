import pygame
from pygame import font


class Button:

	def __init__(self, AlienGame, text):
		self.settings = AlienGame.settings
		self.screen = AlienGame.screen
		self.screen_rect = self.screen.get_rect()


		self.rect = pygame.Rect(0,0, self.settings.BUTTON_WIDTH, self.settings.BUTTON_HEIGHT)
		self.rect.center = self.screen_rect.center

		self.text_to_image(text)

	def text_to_image(self, text):
		self.font = font.SysFont(self.settings.BUTTON_FONT, self.settings.BUTTON_FONT_SIZE)
		self.text_image = self.font.render(text, True, self.settings.BUTTON_TEXT_COLOR)

		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.center = self.rect.center

	def draw(self):
		pygame.draw.rect(self.screen, self.settings.BUTTON_COLOR, self.rect)
		self.screen.blit(self.text_image, self.text_image_rect)
