from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/hello", methods=["GET","POST"])
def hello():
	if request.method == "GET":
		return "Please submit the form instead!"
	name = request.form.get("name")
	return render_template("hello.html", name=name)

if __name__ == '__main__':
	app.run(debug=True)