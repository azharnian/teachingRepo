from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
	return "I'm at home"

@app.route("/about")
def anas():
	return "About Something"

@app.route("/<string:name>")
def hello(name):
	return "Hello, {}".format(name)

app.run(debug=True) #host="0.0.0.0", port="8000", 