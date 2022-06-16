

class GameStatistics:

	def __init__(self, FlappyBird):
		self.my_settings = FlappyBird.my_settings
		self.reset_game()
		self.pre_game = True
		self.game_active = False
		self.high_score = 0
		self.replay = False


	def reset_game(self):
		self.score = 0
		self.level = 1
		self.my_settings.BIRD_LIFE = 3
		self.paused = False
