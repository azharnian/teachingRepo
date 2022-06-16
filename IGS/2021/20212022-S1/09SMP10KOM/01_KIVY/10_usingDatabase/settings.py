import sqlite3

class Settings:

	conn = sqlite3.connect('data/app.db')
	cur = conn.cursor()