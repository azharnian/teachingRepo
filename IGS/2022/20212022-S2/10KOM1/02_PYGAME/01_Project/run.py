import pygame
import sys
from random import choice

pygame.init()

class Settings():

	fps = 25 #tick
	screen_size = (500, 500) 
	screen_bg_color = [107, 52, 235] #fill
	land_speed = 5
	bird_fly_speed = 3
	bird_fall_speed = 1


screen = pygame.display.set_mode(Settings.screen_size)
screen_rect = screen.get_rect()

class Land():

	def __init__(self):

		self.image = pygame.transform.scale(pygame.image.load("images/land.png"), (2*screen_rect.width, screen_rect.height//5))
		self.rect = self.image.get_rect()

		self.rect.midbottom = screen_rect.midbottom

	def move(self):
		self.rect.x -= Settings.land_speed
		if self.rect.centerx <= 0:
			self.rect.left = screen_rect.left

	def show(self):
		screen.blit(self.image, self.rect)

class Bird():

	image = pygame.image.load("images/bird.png")
	rect = image.get_rect()
	rect.center = screen_rect.center
	fly = False
	pass_pipe = False

	@classmethod
	def move(self):
		if self.fly:
			self.rect.y -= Settings.bird_fly_speed
		else:
			self.rect.y += Settings.bird_fall_speed

	@classmethod
	def show(self):
		screen.blit(self.image, self.rect)


land = Land()

class Pipe():

	def __init__(self, position):
		self.rect = pygame.Rect(0, 0, 0.15*screen_rect.width, 0.4*screen_rect.height)
		self.head_rect = pygame.Rect(0, 0, 1.2*self.rect.width, 0.15*self.rect.height)
		self.position = position
		self.color = (0, 200, 0)

		if self.position == "top":
			self.rect.topright = screen_rect.topright
			self.head_rect.midbottom = self.rect.midbottom
		elif self.position == "bottom":
			self.rect.bottomright = screen_rect.bottomright
			self.head_rect.midtop = self.rect.midtop

	def move(self):
		self.rect.x -= 5

		if self.position == "top":
			self.head_rect.midbottom = self.rect.midbottom
		elif self.position == "bottom":
			self.head_rect.midtop = self.rect.midtop


	def show(self):
		pygame.draw.rect(screen, self.color, self.rect)
		pygame.draw.rect(screen, self.color, self.head_rect)

pipes = [ Pipe(position) for position in ["top", "bottom"] ]



def main():
	while True:

		screen.fill(Settings.screen_bg_color)

		Bird.show()
		Bird.move()

		for pipe in pipes:
			if pipe.rect.right <= 0:
				pipes[0].rect.topleft = screen_rect.topright
				pipes[1].rect.bottomleft = screen_rect.bottomright

				random_height = choice([0, 25, 50, 75, 100, 125, 150])
				minimum_height = land.rect.height + (0.1*screen_rect.height)
				new_height_bottom = minimum_height + random_height
				new_height_top = screen_rect.height - new_height_bottom - screen_rect.height//5

				pipes[1].rect = pygame.Rect(0, 0, 0.15*screen_rect.width, new_height_bottom)
				pipes[0].rect = pygame.Rect(0, 0, 0.15*screen_rect.width, new_height_top)

				pipes[1].rect.bottomleft = screen_rect.bottomright
				pipes[0].rect.topleft = screen_rect.topright
			
			pipe.show()
			pipe.move()

		land.show()
		land.move()

		pygame.time.Clock().tick(Settings.fps)
		pygame.display.flip()

		for every_event in pygame.event.get():
			if every_event.type == pygame.QUIT:
				pygame.quit()

			elif every_event.type == pygame.KEYDOWN:
				if every_event.key == pygame.K_SPACE:
					Bird.fly = True

			elif every_event.type == pygame.KEYUP:	
				if every_event.key == pygame.K_SPACE:
					Bird.fly = False

			elif every_event.type == pygame.MOUSEBUTTONDOWN:
				mouse_position = pygame.mouse.get_pos()
				
if __name__ == '__main__':
	main()