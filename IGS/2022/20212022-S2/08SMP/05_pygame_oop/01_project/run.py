import pygame

pygame.init()


# screen = pygame.display.set_mode([500, 500])
# screen_rect = screen.get_rect()

class Screen():

	def __init__(self):
		self.display = pygame.display.set_mode([500, 500])
		self.rect = self.display.get_rect()

	def show(self):
		self.display.fill([107, 52, 235])

screen = Screen()

class Platform():

	def __init__(self):
		self.image = pygame.transform.scale(pygame.image.load("images/land.png"), (2*screen.rect.width, screen.rect.height//4))
		self.rect = self.image.get_rect()

		self.rect.midbottom = screen.rect.midbottom

	def move(self):
		self.rect.x -= 5
		if self.rect.centerx <= 0:
			self.rect.left = screen.rect.left

	def show(self):
		screen.display.blit(self.image, self.rect)

platform = Platform()

def main():

	while True:

		# screen.fill([107, 52, 235])
		screen.show()

		# screen.display.blit(platform, platform_rect)
		# platform_move()

		platform.show()
		platform.move()

		pygame.display.flip()
		pygame.time.Clock().tick(25)

		for every_event in pygame.event.get():
			if every_event.type == pygame.QUIT:
				pygame.quit()

			elif every_event.type == pygame.KEYDOWN:
				
				if every_event.key == pygame.K_SPACE:
					pass

			elif every_event.type == pygame.KEYUP:
				
				if every_event.key == pygame.K_SPACE:
					pass
			elif every_event.type == pygame.MOUSEBUTTONDOWN:
				mouse_position = pygame.mouse.get_pos()

if __name__ == '__main__':
	main()