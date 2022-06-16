from configs.settings import Settings

def main():
	settings = Settings()
	settings.CUR.execute("""
		CREATE TABLE IF NOT EXISTS players (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		username TEXT NOT NULL UNIQUE,
		high_score INTEGER NOT NULL DEFAULT 0,
		created TEXT DEFAULT "" NOT NULL ,
		last_playing TEXT DEFAULT "" NOT NULL )""")

if __name__ == '__main__':
	main()
