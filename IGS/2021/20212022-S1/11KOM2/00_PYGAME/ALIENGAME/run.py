import sys
import time
import pygame

from settings import Settings
from game_stats import Gamestats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienGame:

	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.stats = Gamestats(self)
		#screenmode flag
		self.full_screen_mode_status = False

		self.normal_screen_mode()
		#self.full_screen_mode()
		self.scoreboard = Scoreboard(self)
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

		self.title = pygame.display.set_caption("ALIEN GAME")

		self.play_button = Button(self, "Play")

	def run(self):

		while True:
			self._check_events()

			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()

			self._update_screen()

			
			
	#refactoring methods
	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

			elif event.type == pygame.MOUSEBUTTONDOWN:

				mouse_position = pygame.mouse.get_pos()
				self._check_play_button(mouse_position)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		# elif event.key == pygame.K_f and self.full_screen_mode_status == False:
		# 	self.full_screen_mode()
		# elif event.key == pygame.K_n and self.full_screen_mode_status:
		# 	self.normal_screen_mode()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False
		elif event.key == pygame.K_UP:
			self.ship.moving_up = False

	def _check_play_button(self, mouse_position):
		if self.play_button.rect.collidepoint(mouse_position) and not self.stats.game_active:
			self.stats.reset_stats()
			self.scoreboard.update_score_image()
			self.scoreboard.update_ships_image()
			self.settings.init_dynamic_settings()
			self.stats.game_active = True

			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()
			pygame.mouse.set_visible(False)

	def full_screen_mode(self):
		self.full_screen_mode_status = True
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.SCREEN_WIDTH = self.screen.get_rect().width
		self.settings.SCREEN_HEIGHT = self.screen.get_rect().height

	def normal_screen_mode(self):
		self.full_screen_mode_status = False
		self.settings.SCREEN_WIDTH = 600
		self.settings.SCREEN_HEIGHT = 400
		self.screen = pygame.display.set_mode((self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.BULLETS_ALLOWED:
			bullet = Bullet(self)
			self.bullets.add(bullet)
			# print(len(self.bullets))

	def _update_bullets(self):
		self.bullets.update()

		for bullet in self.bullets.sprites():
			if bullet.rect.bottom < 0:
				self.bullets.remove(bullet)
				# print(len(self.bullets))
		self._check_bullets_aliens_collisions()
		

	def _check_bullets_aliens_collisions(self):
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
		#print(collisions)

		if collisions:
			number_aliens = 0
			for aliens_collisions in collisions.values():
				# for alien in aliens_collisions:
				# 	number_aliens += 1
				number_aliens += len(aliens_collisions)
			# print(number_aliens)
			self.stats.score += self.settings.ALIEN_POINTS * number_aliens
			self.scoreboard.update_score_image()
			self.scoreboard.check_high_score()
			

		if not self.aliens:
			self._create_fleet()
			self.bullets.empty()
			self.settings.increase_speed()

			self.stats.level += 1
			self.scoreboard.update_level_image()

	def _create_fleet(self):
		alien = Alien(self)
		alien_width, alien_height = alien.rect.width, alien.rect.height

		#X AXIS
		available_space_x = self.settings.SCREEN_WIDTH - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		#Y AXIS
		ship_height = self.ship.rect.height
		available_space_y = self.settings.SCREEN_HEIGHT - (3 * ship_height)
		number_rows = available_space_y // (2 * alien_height)

		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_width, alien_height, alien_number, row_number)

	def _create_alien(self, alien_width, alien_height, alien_number, row_number):
		alien = Alien(self)
		#alien_width, alien_height = alien.rect.width, alien.rect.height

		alien.rect.x = alien_width + 2 * alien_width * alien_number
		alien.rect.y = alien_height + 2 * alien_height * row_number

		self.aliens.add(alien)

	def _update_aliens(self):
		self._check_fleet_edges()
		self.aliens.update()

		collision = pygame.sprite.spritecollideany(self.ship, self.aliens)
		if collision:
			# print("ship hit!")
			# sys.exit()
			self._ship_hit()

	def _ship_hit(self):
		self.settings.SHIP_LIMIT -= 1
		self.scoreboard.update_ships_image()
		# print(self.settings.SHIP_LIMIT)
		if self.settings.SHIP_LIMIT > 0:

			self.aliens.empty()
			self.bullets.empty()

			self._create_fleet()
			self.ship.center_ship()

			time.sleep(1)

		else:

			self.stats.game_active = False
			pygame.mouse.set_visible(True)


	def _check_fleet_edges(self):
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._drop_aliens()
				self.settings.ALIEN_SPEED *= -1
				break

	def _drop_aliens(self):
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.ALIEN_DROP
		
	def _update_screen(self):
		self.screen.fill(self.settings.BG_COLOR)
		self.scoreboard.blitme()
		self.ship.blitme()
		if self.stats.game_active:
			for bullet in self.bullets.sprites():
				bullet.draw()

		self.aliens.draw(self.screen)

		if not self.stats.game_active:
			self.play_button.draw()

		pygame.display.flip()
		pygame.time.Clock().tick(30)

if __name__ == '__main__':
	my_game = AlienGame()
	my_game.run()