from datetime import datetime as dt

class Player:

	def __init__(self, username, id=None, high_score=0, created=dt.now(), last_playing=dt.now()):

		self.id = id
		self.username = username
		self.high_score = high_score
		self.created = created
		self.last_playing = last_playing
		#(id, username, high_score, created, last_playing) 