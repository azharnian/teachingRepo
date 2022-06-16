from flask import Flask, render_template, url_for, redirect, flash

from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f10b0e18ba733700d98d19e876f79caab719d8eda3502cf3d46543f780cbad45'





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
	form = RegistrationForm()

	if form.validate_on_submit():
		flash(f"Account created for {form.username.data}!", "success")

	return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
	form = LoginForm()

	return render_template('login.html', title='Login', form=form)

@app.route("/about")
def about():
	return render_template('about.html', title='About Us')


if __name__ == '__main__':
	app.run(debug=True)





