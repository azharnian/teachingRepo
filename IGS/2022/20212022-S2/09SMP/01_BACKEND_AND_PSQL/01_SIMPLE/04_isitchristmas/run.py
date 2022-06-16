from flask import Flask, render_template

from datetime import datetime


app = Flask(__name__)

@app.route("/")
def index():

	now = datetime.now()

	christmas = now.month == 12 and now.day == 25
	# if christmas:
	# 	text = "YES"
	# else:
	# 	text = "NO"

	return render_template("index.html", christmas=christmas)

if __name__ == '__main__':
	app.run(debug=True)