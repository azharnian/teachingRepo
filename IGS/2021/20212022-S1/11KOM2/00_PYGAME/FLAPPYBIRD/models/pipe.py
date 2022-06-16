import pygame

class HeadPipe:

	def __init__(self, width, height):
		self.rect = pygame.Rect(0, 0, width, height)

class Pipe(pygame.sprite.Sprite):

	def __init__(self, FlappyBird):
		super().__init__()
		self.my_settings = FlappyBird.my_settings
		self.my_screen = FlappyBird.my_screen
		self.my_statistics = FlappyBird.my_statistics

		self.rect = pygame.Rect(0, 0, self.my_settings.PIPE_WIDTH, self.my_settings.PIPE_HEIGHT)
		self.rect.topright = self.my_screen.screen_rect.topright
		self.rect.x += (self.my_screen.screen_rect.width // 6)

		self.head = HeadPipe((3*self.rect.width//2), (self.rect.height//10))
		self.head.rect.midbottom = self.rect.midbottom

	def move(self):
		if not self.my_statistics.paused:
			self.rect.x -= self.my_settings.PIPE_SPEED
			self.head.rect.x -= self.my_settings.PIPE_SPEED

	def draw(self):
		pygame.draw.rect(self.my_screen.screen, self.my_settings.PIPE_COLOR, self.rect)
		pygame.draw.rect(self.my_screen.screen, self.my_settings.PIPE_COLOR, self.head.rect)