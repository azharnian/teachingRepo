import pygame
import sys
from random import randint, choice

pygame.init()


screen = pygame.display.set_mode([500, 500])
screen_rect = screen.get_rect()

platform = pygame.image.load("images/land.png")
platform_rect = platform.get_rect()
platform = pygame.transform.scale(platform, (2*screen_rect.width, platform_rect.height))
platform_rect = platform.get_rect()
# platform_rect.y = screen_rect.height - platform_rect.height
# platform_rect.x = screen_rect.width//2 - platform_rect.width//2
platform_rect.midbottom = screen_rect.midbottom

def platform_move():
	platform_rect.x -= 5
	if platform_rect.centerx <= 0:
		platform_rect.left = screen_rect.left


bird = pygame.image.load("images/bird.png")
bird_rect = bird.get_rect()
bird_rect.center = screen_rect.center

bird_fly = False
bird_pass_pipe = False


pipe = pygame.Rect(0, 0, 0.15*screen_rect.width, 0.4*screen_rect.height)
pipe.topright = screen_rect.topright
pipe_head = pygame.Rect(0, 0, 1.2*pipe.width, 0.15*pipe.height)
pipe_head.midbottom = pipe.midbottom

pipe2 = pygame.Rect(0, 0, 0.15*screen_rect.width, 0.4*screen_rect.height)
pipe_head2 = pygame.Rect(0, 0, 1.2*pipe2.width, 0.15*pipe2.height)
pipe2.bottomright = screen_rect.bottomright
pipe_head2.midtop = pipe2.midtop

play_button = pygame.image.load("images/play_button.png")
play_button_rect = play_button.get_rect()
play_button = pygame.transform.scale(play_button, (play_button_rect.width//10, int(0.1*play_button_rect.height)))
play_button_rect = play_button.get_rect()
play_button_rect.center = screen_rect.center
play_button_rect.y += screen_rect.height//10

title_label = pygame.font.Font("fonts/BirdyGame.ttf", 40)
title_label_image = title_label.render("Flappy Bird", True, (255, 255, 255))
title_label_image_rect = title_label_image.get_rect()
title_label_image_rect.center = screen_rect.center
title_label_image_rect.y -= screen_rect.height//10

score = 0
score_label = pygame.font.Font("fonts/BirdyGame.ttf", 20)
score_label_image = score_label.render(f"Score : {score}", True, (255, 255, 255))
score_label_image_rect = score_label_image.get_rect()
score_label_image_rect.topleft = screen_rect.topleft
score_label_image_rect.x += 10
score_label_image_rect.y += 10

lifes = 1
heart = {
	"image" : pygame.transform.scale(pygame.image.load("images/life.png"), (30, 30))
} 
heart["rect"] = heart["image"].get_rect()
hearts = [ heart for _ in range(lifes) ]

def hearts_move():
	global hearts, lifes
	counter = 0
	if lifes > 0:
		for heart in hearts:
			heart['rect'].topright = screen_rect.topright
			heart['rect'].x -= (10*(counter+1)) + (heart['rect'].width*counter)
			heart['rect'].y += 10
			counter += 1
			screen.blit(heart["image"], heart["rect"])


def pipe_move():
	global bird_pass_pipe, screen_rect, platform_rect, pipe, pipe2
	pipe.x -= 5
	pipe2.x -= 5
	# pipe_head.x -= 5
	if pipe.right <= 0:

		pipe2.height = platform_rect.height + (0.1*screen_rect.height) + choice([0, 50, 100, 150]) #randint(50, 200)
		pipe.height = screen_rect.height - pipe2.height - (0.2*screen_rect.height)
		print(screen_rect.height, pipe.height, pipe2.height, 0.2*screen_rect.height)

		pipe = pygame.Rect(0, 0, pipe.width, pipe.height)
		pipe2 = pygame.Rect(0, 0, pipe2.width, pipe2.height)

		# pipe.left = screen_rect.right
		# pipe2.left = screen_rect.right
		pipe.topleft = screen_rect.topright
		pipe2.bottomleft = screen_rect.bottomright

		bird_pass_pipe = False
	pipe_head.midbottom = pipe.midbottom
	pipe_head2.midtop = pipe2.midtop


def bird_move():
	global bird_fly
	if bird_fly:
		# print("Bird is flying")
		bird_rect.y -= 3
	else:
		# print("Bird is falling down.")
		bird_rect.y += 1

def check_bird_point():
	global pipe, bird_rect, score, bird_pass_pipe, score_label_image

	if (pipe.centerx <= bird_rect.centerx) and not bird_pass_pipe:
		# print("passing pipe")
		score += 1
		score_label_image = score_label.render(f"Score : {score}", True, (255, 255, 255))
		bird_pass_pipe = True

def check_bird_hit():
	global pipe, pipe2, pipe_head, pipe_head2, bird_rect, lifes, platform_rect, start

	collide_top_edge = bird_rect.y <= 0
	collide_pipe = bird_rect.colliderect(pipe)
	collide_pipe_head = bird_rect.colliderect(pipe_head)
	collide_pipe2 = bird_rect.colliderect(pipe2)
	collide_pipe_head2 = bird_rect.colliderect(pipe_head2)
	collide_platform = bird_rect.colliderect(platform_rect)

	if collide_top_edge or collide_pipe or collide_pipe_head or collide_pipe2 or collide_pipe_head2 or collide_platform:
		lifes -= 1
		start = False
		sys.exit()
		return True

	return



start = False
def event_listener():
	global bird_fly, play_button_rect, start

	for every_event in pygame.event.get():
		if every_event.type == pygame.QUIT:
			pygame.quit()

		elif every_event.type == pygame.KEYDOWN:
			
			if every_event.key == pygame.K_SPACE:
				bird_fly = True

		elif every_event.type == pygame.KEYUP:
			
			if every_event.key == pygame.K_SPACE:
				bird_fly = False

		elif every_event.type == pygame.MOUSEBUTTONDOWN:

			mouse_position = pygame.mouse.get_pos()
			# print(mouse_position)
			if play_button_rect.collidepoint(mouse_position) and not start:
				# print("inside")
				start = True


def mainloop():
	global bird_fly, start, hearts, pipe, pipe_head, pipe2, pipe_head2

	while True:
		screen.fill([107, 52, 235]) #RGB -> Green

		screen.blit(bird, bird_rect)
		check_bird_point()	
		check_bird_hit()

		pygame.draw.rect(screen, (0, 200, 0), pipe)
		pygame.draw.rect(screen, (0, 200, 0), pipe_head)
		pygame.draw.rect(screen, (0, 200, 0), pipe2)
		pygame.draw.rect(screen, (0, 200, 0), pipe_head2)

		screen.blit(platform, platform_rect)	

		screen.blit(score_label_image, score_label_image_rect)

		hearts_move()

		if start:
			bird_move()
			pipe_move()
			platform_move()
		else:
			screen.blit(play_button, play_button_rect)
			screen.blit(title_label_image, title_label_image_rect)	

		pygame.time.Clock().tick(25)
		pygame.display.flip()

		event_listener()

mainloop()

