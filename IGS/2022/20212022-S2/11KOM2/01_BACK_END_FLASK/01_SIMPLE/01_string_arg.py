from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "I'm at home"

@app.route("/about")
def about():
	return "about something"


@app.route("/<string:name>")
def hello(name):
	name = name.title()
	return "Hello, {}".format(name)


if __name__ == "__main__":
	app.run()