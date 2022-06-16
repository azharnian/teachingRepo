from flask import Flask, render_template

app  = Flask(__name__)

@app.route("/")
def index():
	number = 13

	isOdd = number%2 != 0
	# return render_template("index.html", number=number)
	return render_template("index.html", isOdd=isOdd)

if __name__ == '__main__':
	app.run(debug=True)