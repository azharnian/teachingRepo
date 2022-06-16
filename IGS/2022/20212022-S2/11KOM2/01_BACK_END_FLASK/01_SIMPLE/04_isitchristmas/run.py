from flask import Flask, render_template

from datetime import datetime


app = Flask(__name__)


@app.route("/")
def index():

	now = datetime.now()

	isItChristmas = now.day == 25 and now.month == 12

	return render_template("index.html", isItChristmas=isItChristmas)


if __name__ == "__main__":
	app.run(debug=True)