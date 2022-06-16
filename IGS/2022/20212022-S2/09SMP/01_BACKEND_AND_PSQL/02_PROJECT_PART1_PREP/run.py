from flask import Flask, render_template, url_for, redirect, flash
app = Flask(__name__)


tweets = [
	{
		'author' : 'Budi Doremi',
		'content' : 'This is my first tweet',
		'date_posted' : 'May 10, 2022'
	},
	{
		'author' : 'Alex Chandra',
		'content' : 'Hello World',
		'date_posted' : 'May 11, 2022'
	}
]


@app.route("/") # 127.0.0.1:8000
@app.route("/home") # 127.0.0.1:8000/home
def home():
	return render_template('home.html', tweets=tweets)

@app.route("/register", methods=['GET', 'POST'])
def register():
	return render_template('register.html', title='Register')


@app.route("/login")
def login():
	return render_template('login.html', title='Login')

@app.route("/about")
def about():
	return render_template('about.html', title='About Us')


if __name__ == '__main__':
	app.run(debug=True)





