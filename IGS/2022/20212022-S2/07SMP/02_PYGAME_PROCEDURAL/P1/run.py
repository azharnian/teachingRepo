import pygame
import sys

screen = pygame.display.set_mode((500, 500))
screen_rect = screen.get_rect()

bird = pygame.image.load("images/bird.png")
bird_rect = bird.get_rect() #virt pos and size
# bird_rect.x += 230
# bird_rect.y += 230
bird_rect.center = screen_rect.center

land = pygame.image.load("images/land.png")
land = pygame.transform.scale(land, (2*500, 86))
land_rect = land.get_rect()
land_rect.midbottom = screen_rect.midbottom

pipe = pygame.image.load("images/pipe.png")
pipe = pygame.transform.scale(pipe, (63 ,243))
pipe_rect = pipe.get_rect()
pipe_rect.bottomright = screen_rect.bottomright

pipe_2 = pygame.image.load("images/pipe.png")
pipe_2 = pygame.transform.scale(pipe_2, (63 ,200))
pipe_2 = pygame.transform.rotate(pipe_2, -180)
pipe_rect_2 = pipe_2.get_rect()
pipe_rect_2.topright = screen_rect.topright

def land_move():
	land_rect.x -= 5
	if land_rect.centerx <= 0:
		land_rect.bottomleft = screen_rect.bottomleft
	# if land_rect.x <= -250:
	# 	land_rect.x = 0

from random import randint

def pipe_move():
	global pipe_rect, pipe, screen_rect, land_rect, pipe_2, pipe_rect_2
	pipe_rect.x -= 10
	pipe_rect_2.x -= 10

	if pipe_rect.right <= screen_rect.left:
		random_height = randint(0, 150)
		minimum_height = land_rect.height + 100

		new_height_pipe = minimum_height+random_height

		gap = 70
		new_height_pipe_2 = screen_rect.height - new_height_pipe - gap

		pipe = pygame.transform.scale(pipe, (pipe_rect.width, new_height_pipe))
		pipe_rect = pipe.get_rect()

		pipe_2 = pygame.transform.scale(pipe_2, (pipe_rect_2.width, new_height_pipe_2))
		pipe_rect_2 = pipe_2.get_rect()

		pipe_rect.bottomleft = screen_rect.bottomright
		pipe_rect_2.topleft = screen_rect.topright

bird_fly = False
def bird_move():
	if bird_fly:
		bird_rect.y -= 3
	else:
		bird_rect.y += 1

while True:

	screen.fill((235, 52, 177))
	screen.blit(bird, bird_rect)
	screen.blit(pipe, pipe_rect)
	screen.blit(pipe_2, pipe_rect_2)
	screen.blit(land, land_rect)

	pipe_move()
	land_move()
	bird_move()

	pygame.display.flip() #redraw and clear screen
	pygame.time.Clock().tick(25) #fps

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			# print("KEYDOWN")
			if event.key == pygame.K_SPACE:
				# print("FLY")
				bird_fly = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				bird_fly = False



