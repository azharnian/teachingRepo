from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():

	return render_template("index.html")


@app.route("/hello")
def hello():

	name = request.args.get("name")
	if name: 
		return render_template("hello.html", name=name)
	return redirect(url_for("index"))


@app.route("/search")
def search():

	query = request.args.get("query")
	return redirect("https://www.google.com/search?q="+query)


if __name__ == "__main__":
	app.run(debug=True)