
class Gamestats:

	def __init__(self, AlienGame):
		self.settings = AlienGame.settings
		self.game_active = False
		self.score = 0
		self.high_score = 0
		self.level = 1
		self.reset_stats()

	def reset_stats(self):
		self.settings.SHIP_LIMIT = 5
		self.score = 0