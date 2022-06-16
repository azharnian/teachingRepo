import bcrypt
from getpass import getpass

from settings import Settings
from employee import Employee


def main():
	app_settings = Settings()
	app_settings.CUR.execute("""
		CREATE TABLE IF NOT EXISTS employees (
			id INT PRIMARY KEY,
			username TEXT,
			password TEXT,
			first TEXT,
			last TEXT,
			salary INTEGER
			)
		""")
	app_settings.CUR.execute("SELECT * FROM employees WHERE username = :username", {"username":"admin"})
	admin = app_settings.CUR.fetchone()

	if not admin:
		admin = Employee("admin", "admin", "", 2500000)
		password = getpass("Input admin password\nPassword : ")
		retype_password = getpass("Retype Password : ")
		attempts = 0
		while retype_password != password:
			print("Password doesn't match!")
			attempts += 1
			retype_password = getpass("Retype Password : ")
			if attempts == 3:
				print("Limit Exceeded, Please try again later.")
				break
		else:
			admin.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
			app_settings.CUR.execute("""INSERT INTO employees 
							VALUES (:id, :username, :password, :first, :last, :salary)
							""", {
							"id" : admin.id,
							"username" : admin.username,
							"password" : admin.password,
							"first" : admin.first,
							"last" : admin.last,
							"salary" : admin.salary
							})
			app_settings.CONN.commit()
			print("Init DB Done!")
	else:
		print("Admin Already Exists!")



if __name__ == '__main__':
	main()