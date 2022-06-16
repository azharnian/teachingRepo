
class Settings:

	def __init__(self):

		#SCREEN SETTING

		self.SCREEN_WIDTH = 600
		self.SCREEN_HEIGHT = 400
		self.BG_COLOR = (230, 230, 230)

		#SHIP SETTING
		self.SHIP_LIMIT = 5

		#BULLET SETTING
		self.BULLET_WIDTH = 100
		self.BULLET_HEIGHT = 15
		self.BULLET_COLOR = (60, 60, 60)
		self.BULLETS_ALLOWED = 5

		#ALIEN SETTINGS
		self.ALIEN_DROP = 15

		#BUTTON SETTINGS
		self.BUTTON_WIDTH = 200
		self.BUTTON_HEIGHT = 50
		self.BUTTON_COLOR = (0, 255, 0) #RGB
		self.BUTTON_TEXT_COLOR = (255, 255, 255)
		self.BUTTON_FONT = None
		self.BUTTON_FONT_SIZE = 48

		#SCORE DISP SETTINGS
		self.SCORE_TEXT_COLOR = (30, 30, 30)
		self.SCORE_FONT = None
		self.SCORE_FONT_SIZE = 48

		self.speed_scale = 2
		self.score_scale = 1.5
		self.init_dynamic_settings()


	def init_dynamic_settings(self):
		self.SHIP_SPEED = 5
		self.BULLET_SPEED = 3
		self.ALIEN_SPEED = 2
		self.ALIEN_POINTS = 50

	def increase_speed(self):
		self.SHIP_SPEED *= self.speed_scale
		self.BULLET_SPEED *= self.speed_scale
		self.ALIEN_SPEED *= self.speed_scale
		self.ALIEN_POINTS = int(self.ALIEN_POINTS * self.score_scale)

