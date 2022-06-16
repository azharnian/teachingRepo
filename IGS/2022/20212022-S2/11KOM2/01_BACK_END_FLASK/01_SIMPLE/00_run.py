from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello, World!"

@app.route("/anas")
def anas():
	return "Hello, Anas!"

@app.route("/html")
def html():
	return "<h1>Hello, Saori ...</h1>"

@app.route("/more_html")
def more_html():
	return """
			<h1>Hello, Steven</h1><br>
			<p>Adios...</p>
			"""


app.run(debug=True)