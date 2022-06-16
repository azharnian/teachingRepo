from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
	return "Hello, world!"

@app.route("/anas")
def anas():
	return "Hello, Anas!"

@app.route("/html")
def html():
	return "<h1>Hello, Ria!</h1>"

if __name__ == "__main__":
	app.run(debug=True)