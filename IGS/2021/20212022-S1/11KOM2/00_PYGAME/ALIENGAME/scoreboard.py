import pygame
from pygame import font

from ship import Ship


class Scoreboard:

	def __init__(self, AlienGame):
		self.game = AlienGame
		self.settings = AlienGame.settings
		self.screen = AlienGame.screen
		self.screen_rect = self.screen.get_rect()
		self.stats = AlienGame.stats

		self.font = font.SysFont(self.settings.SCORE_FONT, self.settings.SCORE_FONT_SIZE)

		self.update_score_image()
		self.update_high_score_image()
		self.update_level_image()


		self.ships = pygame.sprite.Group()
		self.update_ships_image()


	def update_ships_image(self):
		self.ships.empty()
		ship = Ship(self.game)
		ship.image = pygame.transform.scale(ship.image, (ship.rect.width//3, ship.rect.height//3))
		ship.rect = ship.image.get_rect()
		ship_width = ship.rect.width
		for avery_ship in range(self.settings.SHIP_LIMIT):
			ship = Ship(self.game)
			ship.image = pygame.transform.scale(ship.image, (ship.rect.width//3, ship.rect.height//3))
			ship.rect = ship.image.get_rect()
			ship.rect.x = self.screen_rect.left + 10 + (avery_ship * ship_width)
			ship.rect.y = 5
			self.ships.add(ship)


	def update_score_image(self):
		self.score_image = self.font.render(str(self.stats.score), True, self.settings.SCORE_TEXT_COLOR)

		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.topright = self.screen_rect.topright

		self.score_image_rect.y += 20
		self.score_image_rect.x -= 20


	def update_high_score_image(self):
		self.high_score_image = self.font.render(str(self.stats.high_score), True, self.settings.SCORE_TEXT_COLOR)

		self.high_score_image_rect = self.high_score_image.get_rect()
		self.high_score_image_rect.midtop = self.screen_rect.midtop

		self.high_score_image_rect.y += 20

	def update_level_image(self):
		self.level_image = self.font.render(str(self.stats.level), True, self.settings.SCORE_TEXT_COLOR)
		self.level_image_rect = self.level_image.get_rect()
		self.level_image_rect.midtop = self.score_image_rect.midbottom

		self.level_image_rect.y +=20
		self.level_image_rect.right = self.screen_rect.right - 20


	def check_high_score(self):
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.update_high_score_image()


	def blitme(self):
		self.screen.blit(self.score_image, self.score_image_rect)
		self.screen.blit(self.high_score_image, self.high_score_image_rect)
		self.screen.blit(self.level_image, self.level_image_rect)
		self.ships.draw(self.screen)

