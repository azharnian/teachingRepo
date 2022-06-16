import bcrypt
from getpass import getpass

from settings import Settings
from models.user import User


def main():

	settings = Settings()
	settings.cur.execute("""
		CREATE TABLE IF NOT EXISTS users (
		id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		username TEXT NOT NULL UNIQUE,
		password TEXT NOT NULL,
		first TEXT NOT NULL,
		last TEXT NOT NULL,
		bio TEXT DEFAULT "" NOT NULL,
		interest TEXT DEFAULT "" NOT NULL,
		pic TEXT DEFAULT "default.jpg" NOT NULL
		)
		""")
	settings.cur.execute(""" SELECT * FROM users WHERE username = "admin" """)
	admin = settings.cur.fetchone()

	if not admin:
		admin = User(username="admin", first="super", last="admin")
		password = getpass("password : ")
		retype_password = getpass("retype\npassword : ")
		attempts = 0
		while retype_password != password:
			print("password doesn't match")
			attempts += 1
			retype_password = getpass("retype\npassword : ")
			if attempts == 3:
				print("limit exceeded, please re-run script.")
				break
		else:
			admin.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
			settings.cur.execute(""" 
				INSERT INTO users (username, password, first, last)
				VALUES (:username, :password, :first, :last)""",
				{
				"username" : admin.username,
				"password" : admin.password,
				"first" : admin.first,
				"last" : admin.last
				})
			settings.conn.commit()
			print("init DB app DONE!")
	else:
		print("admin already exists.")



if __name__ == "__main__":
	main()