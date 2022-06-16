import pygame

class Button:

	def __init__(self, FlappyBird, text):
		self.my_settings = FlappyBird.my_settings
		self.my_screen = FlappyBird.my_screen

		self.rect = pygame.Rect(0,0, self.my_settings.BUTTON_WIDTH, self.my_settings.BUTTON_HEIGHT)
		self.font_file = self.my_settings.BUTTON_FONT
		self.color = self.my_settings.BUTTON_COLOR
		self.text_to_image(text)

	def text_to_image(self, text):

		self.font = pygame.font.Font(self.font_file, self.my_settings.BUTTON_FONT_SIZE)
		self.text_image = self.font.render(text, True, self.my_settings.BUTTON_FONT_COLOR)

		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.center = self.rect.center

	def draw(self):
		pygame.draw.rect(self.my_screen.screen, self.color, self.rect)
		self.my_screen.screen.blit(self.text_image, self.text_image_rect)


class PlayButton:

	def __init__(self, FlappyBird):
		self.my_settings = FlappyBird.my_settings
		self.my_screen = FlappyBird.my_screen

		self.image = pygame.image.load("images/pause_button.png")
		self.rect = self.image.get_rect()

		self.image = pygame.transform.scale(self.image, (self.rect.width//3, self.rect.height//3))
		self.rect = self.image.get_rect()

		self.rect.topright = self.my_screen.screen_rect.topright
		self.rect.x -= 20
		self.rect.y += 15

	def blit(self):
		self.my_screen.screen.blit(self.image, self.rect)








