import bcrypt
from getpass import getpass

from settings import Settings
from models.user import User

def main ():

	settings = Settings() #constraint NOT NULL, UNIQUE
	settings.cur.execute("""
		CREATE TABLE IF NOT EXISTS users (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			username TEXT NOT NULL UNIQUE,
			password TEXT NOT NULL,
			first TEXT NOT NULL,
			last TEXT NOT NULL,
			bio TEXT DEFAULT "" NOT NULL,
			interest TEXT DEFAULT "" NOT NULL,
			pic TEXT DEFAULT "default.png" NOT NULL)
		""") #doc string / comment, multiplelines comment
	settings.cur.execute("""SELECT * FROM users WHERE username = "admin" """)
	user = settings.cur.fetchone()

	if not user:
		admin = User(username="admin", first="super", last="admin")
		password = getpass("Input New Password for Admin\npassword : ")
		retype_password = getpass("Retype\npassword : ")
		attempts = 0
		while retype_password != password:
			if attempts == 3:
				print("limit exceeded, please try again.")
				break

			print("password doesn't match")
			attempts += 1
			retype_password = getpass("Retype\npassword : ")
		else:
			admin.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
			settings.cur.execute(""" 
				INSERT INTO users (username, password, first, last)
				VALUES (:username, :password, :first, :last)
				""", {
				"username" : admin.username,
				"password" : admin.password,
				"first" : admin.first,
				"last" : admin.last
				})
			settings.conn.commit()
			print("Done ...")

	else:
		print("admin already exists.")


if __name__ == '__main__':
	main()