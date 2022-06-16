from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	text = "Hello, world!"
	return render_template("index.html", text=text)

if __name__ == "__main__":
	app.run()