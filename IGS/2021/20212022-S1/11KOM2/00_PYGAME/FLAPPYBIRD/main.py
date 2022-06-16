import sys
from random import randint
from datetime import datetime as dt

import pygame
from configs.settings import Settings
from configs.screen import Screen
from configs.game_statistics import GameStatistics
from configs.scoreboard import ScoreBoard

from uix.button import Button, PlayButton
from uix.label import Label
from uix.entry import Entry

from models.platform import Platform
from models.pipe import Pipe
from models.bird import Bird
from models.player import Player

class FlappyBird:

	def __init__(self):
		pygame.init()
		self.my_settings = Settings()
		self.my_statistics = GameStatistics(self)
		self.my_screen = Screen(self)
		self.my_scoreboard = ScoreBoard(self)

		self.username_label = Label(self, "Player")
		self.username_entry = Entry(self, "")

		self.player = None

		self.login_button = Button(self, "Login")

		self.my_platforms = pygame.sprite.Group()
		self.create_platforms()

		self.my_pipes = pygame.sprite.Group()
		self.create_pipes()

		self.my_bird = Bird(self)

		self.play_button = Button(self, "PLAY")
		self.play_again_button = Button(self, "PLAY AGAIN")
		self.quit_button = Button(self, "QUIT")
		self.play_pause_button = PlayButton(self)

		pygame.mixer.music.load("sounds/backsound.wav")
		pygame.mixer.music.set_volume(.05)
		pygame.mixer.music.play(loops=-1) # looping (-1), no looping (0)


	def _update_screen(self):
		self.my_screen.show()

		if self.my_statistics.pre_game:
			
			self._update_username_label()
			self._update_username_entry()
			self._update_login_button()

		else:
			self._update_bird()

			if self.my_statistics.game_active:
				self._update_pipes()
				self.my_scoreboard.blit()
				self.play_pause_button.blit()

			if not self.my_statistics.game_active:
				if not self.my_statistics.replay:
					self._update_play_button()
				else:
					self._update_play_again_button()
					self._update_quit_button()
					
			if self.my_statistics.paused:
				self._update_play_again_button()
				self._update_quit_button()

			self._update_platforms()

		pygame.display.flip()
		pygame.time.Clock().tick(30)

	def _update_username_label(self):
		self.username_label.text_image_rect.center = self.my_screen.screen_rect.center
		self.username_label.text_image_rect.y -= self.my_screen.screen_rect.height // 6
		self.username_label.blit()


	def _update_username_entry(self):
		self.username_entry.rect.center = self.my_screen.screen_rect.center
		self.username_entry.rect.y = self.username_label.text_image_rect.y + 50
		self.username_entry.text_image_rect.center = self.username_entry.rect.center
		self.username_entry.draw()


	def _update_login_button(self):
		self.login_button.rect.center = self.my_screen.screen_rect.center
		self.login_button.rect.y = self.username_entry.rect.y + 80
		self.login_button.text_image_rect.center = self.login_button.rect.center
		self.login_button.draw()


	def _update_play_button(self):
		self.play_button.rect.center = self.my_screen.screen_rect.center
		self.play_button.text_image_rect.center = self.play_button.rect.center
		self.play_button.draw()

	def _update_play_again_button(self):
		self.play_again_button.rect.center = self.my_screen.screen_rect.center
		self.play_again_button.rect.y -= self.my_screen.screen_rect.height // 8
		self.play_again_button.text_image_rect.center = self.play_again_button.rect.center
		self.play_again_button.draw()

	def _update_quit_button(self):
		self.quit_button.rect.center = self.my_screen.screen_rect.center
		self.quit_button.rect.y += self.my_screen.screen_rect.height // 8
		self.quit_button.text_image_rect.center = self.quit_button.rect.center
		self.quit_button.draw()


	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				if self.my_statistics.pre_game:
					self._check_click_username_entry(mouse_pos)
					self._check_click_login_botton(mouse_pos)
				if not self.my_statistics.replay:
					self._check_click_play_button(mouse_pos)
				else:
					self._check_click_play_again_button(mouse_pos)
					self._check_click_quit_button(mouse_pos)
				if self.my_statistics.game_active:
					self._check_click_play_pause_button(mouse_pos)
	"""
	1. Backsound
	2. Pause and Resume button
	3. Level Speed

	"""

	def _check_keydown_events(self, event):
		if self.my_statistics.pre_game:
			if self.username_entry.active:
				if event.key == pygame.K_BACKSPACE:
					self.username_entry.text = self.username_entry.text[0:-1]
				else:
					if len(self.username_entry.text) < 6:
						self.username_entry.text += event.unicode
				self.username_entry.update()

		if event.key == pygame.K_SPACE:
			self.my_bird.fly = True

	def _check_keyup_events(self, event):
		if event.key == pygame.K_SPACE:
			self.my_bird.fly = False

	def _check_click_username_entry(self, mouse_pos):
		if self.username_entry.rect.collidepoint(mouse_pos):
			self.username_entry.active = True
		else:
			self.username_entry.active = False
		if self.username_entry.active:
			self.username_entry.color = self.my_settings.ENTRY_COLOR_ACTIVE
		else:
			self.username_entry.color = self.my_settings.ENTRY_COLOR_INACTIVE

	def find_players_by_username(self, username):
		with self.my_settings.CONN:
			self.my_settings.CUR.execute("""
				SELECT * FROM players WHERE username=:username
				""", {"username":username})
			return self.my_settings.CUR.fetchone()

	def insert_new_player(self, player):
		with self.my_settings.CONN:
			self.my_settings.CUR.execute("""
				INSERT INTO players (username, created, last_playing)
				VALUES (:username, :created, :last_playing)
				""", {"username":player.username, "created":str(player.created), "last_playing":str(player.last_playing)})
			return True

	def update_last_playing_player(self):
		#jangan lupa import from datetime import datetime as dt di atas!
		with self.my_settings.CONN:
			self.my_settings.CUR.execute("""
				UPDATE players SET last_playing=:last_playing WHERE username=:username
				""",{"last_playing":self.player.last_playing, "username":self.player.username})

	def _check_click_login_botton(self, mouse_pos):
		username = self.username_entry.text.strip()
		print(username)
		if self.login_button.rect.collidepoint(mouse_pos) and username:
			found_player = self.find_players_by_username(username)
			if not found_player:
				self.player = Player(username)
				self.insert_new_player(self.player)
			else:
				self.player = Player(found_player[1], found_player[0], found_player[2], found_player[3], str(dt.now()))
				self.update_last_playing_player()
				self.my_statistics.high_score = self.player.high_score
				self.my_scoreboard.update_high_score_image()	
			self.my_statistics.pre_game = False
		# print(self.username_entry.text)

	def _check_click_play_button(self, mouse_pos):
		if self.play_button.rect.collidepoint(mouse_pos) and not self.my_statistics.game_active and not self.my_statistics.replay:
			self.my_statistics.game_active = True

	def _check_click_play_again_button(self, mouse_pos):
		if self.play_again_button.rect.collidepoint(mouse_pos) and not self.my_statistics.game_active and self.my_statistics.replay:
			self.my_statistics.reset_game()
			self.my_pipes.empty()
			self.create_pipes()
			self.my_bird.reposition()
			self.my_bird.passing_pipe = False
			self.my_scoreboard.update_score_image()
			self.my_statistics.game_active = True

	def _check_click_quit_button(self, mouse_pos):
		if self.quit_button.rect.collidepoint(mouse_pos) and not self.my_statistics.game_active and self.my_statistics.replay:
			sys.exit()

	def _check_click_play_pause_button(self, mouse_pos):
		if self.play_pause_button.rect.collidepoint(mouse_pos):
			self.my_statistics.paused = not self.my_statistics.paused
			if self.my_statistics.paused:
				pygame.mixer.music.pause()
				self.play_pause_button.image = pygame.image.load("images/play_button.png")
			else:
				pygame.mixer.music.unpause()
				self.play_pause_button.image = pygame.image.load("images/pause_button.png")
			self.play_pause_button.image = pygame.transform.scale(self.play_pause_button.image, self.play_pause_button.rect.size)

	def update_high_score_player(self):
		with self.my_settings.CONN:

			self.my_settings.CUR.execute("""
				UPDATE players SET high_score=:high_score WHERE username=:username
				""",{"high_score":self.player.high_score, "username":self.player.username})

	def check_bird_point(self):
		for pipe in self.my_pipes.sprites():
			if (pipe.rect.centerx <= self.my_bird.rect.centerx) and not self.my_bird.passing_pipe:
				#print("pass")
				self.my_statistics.score += 10
				if self.my_statistics.high_score < self.my_statistics.score:
					self.my_statistics.high_score = self.my_statistics.score
					self.my_scoreboard.update_high_score_image()
					self.player.high_score = self.my_statistics.high_score
					self.update_high_score_player()
				self.my_scoreboard.update_score_image()
				self.my_bird.passing_pipe = True
				win_sound = pygame.mixer.Sound("sounds/win_sound.wav")
				win_sound.set_volume(.05)
				win_sound.play()

	def check_bird_hit(self):
		collision_pipe = pygame.sprite.spritecollideany(self.my_bird, self.my_pipes)
		collision_platform = pygame.sprite.spritecollideany(self.my_bird, self.my_platforms)
		for pipe in self.my_pipes.sprites():
			if pipe.head.rect.collidepoint(self.my_bird.rect.x, self.my_bird.rect.y):
				#sys.exit()
				self.my_statistics.game_active = False
				self.my_statistics.replay = True
				hit_sound = pygame.mixer.Sound("sounds/hit_sound.wav")
				hit_sound.set_volume(.05)
				hit_sound.play()

		if collision_pipe or collision_platform or self.my_bird.rect.top <= 0:
			#sys.exit()
			self.my_statistics.game_active = False
			self.my_statistics.replay = True
			hit_sound = pygame.mixer.Sound("sounds/hit_sound.wav")
			hit_sound.set_volume(.05)
			hit_sound.play()
	
	def _update_platforms(self):
		self.my_platforms.draw(self.my_screen.screen)
		for platform in self.my_platforms.sprites():
			platform.move()

	def create_platforms(self):
		number_of_platform = 2
		for each_platform in range(number_of_platform):
			platform = Platform(self)
			platform.rect.x = each_platform * self.my_screen.screen_rect.width
			self.my_platforms.add(platform)

	def _update_pipes(self):
		for pipe in self.my_pipes.sprites():
			pipe.draw()
			pipe.move()
			if pipe.rect.x <= -100:
				self.my_pipes.empty()
				self.create_pipes()
				self.my_bird.passing_pipe = False
		# print(self.my_pipes)

	def create_pipes(self):
		number_of_pipe = 2
		gap = self.my_screen.screen_rect.height // 5
		height_top_pipe = randint(gap, 2*gap)

		for each_pipe in range(number_of_pipe):
			pipe = Pipe(self)

			if each_pipe == 0:
				pipe.rect.height = height_top_pipe
				pipe.head.rect.midbottom = pipe.rect.midbottom

			else:
				pipe.rect.height = self.my_screen.screen_rect.height - height_top_pipe - gap
				pipe.rect.bottomright = self.my_screen.screen_rect.bottomright
				pipe.rect.x += (self.my_screen.screen_rect.width//6)
				pipe.head.rect.midtop = pipe.rect.midtop

			self.my_pipes.add(pipe)

	def _update_bird(self):
		self.my_bird.blit()
		if self.my_statistics.game_active:
			self.my_bird.flying()
			self.check_bird_point()
			self.check_bird_hit()

	def run(self):
		
		while True:
			self.check_events()
			self._update_screen()

if __name__ == '__main__':
	flappy = FlappyBird()
	flappy.run()
	flappy.my_settings.CONN.close()
