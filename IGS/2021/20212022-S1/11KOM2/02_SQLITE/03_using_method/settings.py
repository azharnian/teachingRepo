import sqlite3

class Settings:

	conn = sqlite3.connect("employee.db")
	cur = conn.cursor()

	cur.execute("""
		CREATE TABLE IF NOT EXISTS employees (
		first TEXT,
		last TEXT,
		salary INTEGER)
		""")