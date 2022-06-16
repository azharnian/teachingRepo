import pygame
from pygame.locals import QUIT

pygame.init()


screen = pygame.display.set_mode([500, 500])
screen_rect = screen.get_rect()

platform = pygame.image.load("images/land.png") # load image
platform_rect = platform.get_rect() #get old size
platform = pygame.transform.scale(platform, (2*screen_rect.width, platform_rect.height)) #scale image
platform_rect = platform.get_rect() #get new size

platform_rect.midbottom = screen_rect.midbottom


pipe = pygame.Rect(0, 0, 60, 200)
pipe.topright = screen_rect.topright
pipe_head = pygame.Rect(0, 0, 1.2*pipe.width, 0.15*pipe.height)
pipe_head.midbottom = pipe.midbottom

pipe_2 = pygame.Rect(0, 0, 60, 200)
pipe_2.bottomright = screen_rect.bottomright
pipe_head_2 = pygame.Rect(0, 0, 1.2*pipe_2.width, 0.15*pipe_2.height)
pipe_head_2.midtop = pipe_2.midtop

def platform_move():
	platform_rect.x  = platform_rect.x - 5
	if platform_rect.centerx <= 0:
		platform_rect.left = screen_rect.left

def pipe_move():
	global bird_pass_pipe
	pipe.x -= 5
	pipe_2.x -= 5
	if pipe.right <= 0:
		bird_pass_pipe = False
		pipe.left = screen_rect.right
		pipe_2.left = screen_rect.right
	pipe_head.midbottom = pipe.midbottom
	pipe_head_2.midtop = pipe_2.midtop



bird = pygame.image.load("images/bird.png")
bird_rect = bird.get_rect()
bird_fly = False
bird_pass_pipe = False

bird_rect.center = screen_rect.center

def bird_move():
	global bird_fly

	if bird_fly:
		bird_rect.y -= 3 # bird is flying
	else:
		bird_rect.y += 2 # bird is falling down

def check_bird_point():
	global bird_rect, pipe, pipe_2, bird_pass_pipe, score, score_label_image

	if (bird_rect.centerx >= pipe.centerx or bird_rect.centerx >= pipe_2.centerx) and not bird_pass_pipe:
		score += 1
		score_label_image = score_label.render(f"Score : {score}", True, (255, 255, 255))
		bird_pass_pipe = True

import sys
def check_bird_hit():
	global bird_rect, pipe, pipe_head, pipe_2, pipe_head_2, platform_rect, life, hearts, hit

	collide_pipe = bird_rect.colliderect(pipe) or bird_rect.colliderect(pipe_head)
	collide_pipe_2 = bird_rect.colliderect(pipe_2) or bird_rect.colliderect(pipe_head_2)
	collide_platform = bird_rect.colliderect(platform_rect)

	if (collide_pipe or collide_pipe_2 or collide_platform) and not hit:
		hit = True
		life -= 1
		hearts.pop()
		# sys.exit()

hit = False
life = 1
heart = {
	"image" : pygame.image.load("images/heart.png"),
	"rect" : pygame.image.load("images/heart.png").get_rect()
}
hearts = []
for i in range(life):
	heart["rect"].topright = screen_rect.topright
	hearts.append(heart)

# hearts = [ heart for i in range(life) ]


title_label = pygame.font.Font("fonts/BirdyGame.ttf", 60)
title_label_image = title_label.render("Flappy You", True, (255, 255, 255))
title_label_image_rect = title_label_image.get_rect()
title_label_image_rect.center = screen_rect.center
title_label_image_rect.y -= 50

play_button = pygame.image.load("images/play_button.png")
play_button_rect = play_button.get_rect()

play_button = pygame.transform.scale(play_button, (100, 100))
play_button_rect = play_button.get_rect()

play_button_rect.center = screen_rect.center
play_button_rect.y += 50

score = 0
score_label = pygame.font.Font("fonts/BirdyGame.ttf", 30)
score_label_image = score_label.render(f"Score : {score}", True, (255, 255, 255))
score_label_image_rect = score_label_image.get_rect()
score_label_image_rect.topleft = screen_rect.topleft

score_label_box = pygame.Rect(0, 0, score_label_image_rect.width+10, score_label_image_rect.height+5)
score_label_box.center = score_label_image_rect.center

start = False
def mainloop():
	global bird_fly, play_button_rect, start, hearts

	while True:
		screen.fill([107, 52, 235]) #RGB -> Green

		screen.blit(bird, bird_rect)
		
		pygame.draw.rect(screen, (255, 255, 255), pipe)
		pygame.draw.rect(screen, (255, 255, 255), pipe_head)
		pygame.draw.rect(screen, (255, 255, 255), pipe_2)
		pygame.draw.rect(screen, (255, 255, 255), pipe_head_2)
		

		screen.blit(platform, platform_rect)
			

		pygame.draw.rect(screen, (0, 200, 0), score_label_box)
		screen.blit(score_label_image, score_label_image_rect)

		# screen.blit(heart_image, heart_image_rect)

		for heart in hearts:
			screen.blit(heart["image"], heart["rect"])

		if not start:

			screen.blit(title_label_image, title_label_image_rect)

			screen.blit(play_button, play_button_rect)

		else:
			bird_move()
			check_bird_point()
			check_bird_hit()

			pipe_move()
			platform_move()


		pygame.display.flip()

		pygame.time.Clock().tick(25)

		for every_event in pygame.event.get():
			if every_event.type == QUIT:
				pygame.quit()

			elif every_event.type == pygame.KEYDOWN:
				
				if every_event.key == pygame.K_SPACE:
					bird_fly = True

			elif every_event.type == pygame.KEYUP:
				
				if every_event.key == pygame.K_SPACE:
					bird_fly = False

			elif every_event.type == pygame.MOUSEBUTTONDOWN:

				mouse_position = pygame.mouse.get_pos()
				if play_button_rect.collidepoint(mouse_position) and not start:
					start = True




mainloop()

