from flask import render_template, url_for, redirect, flash

from project import app, db #, bcrypt
from project.models import User, Tweet
from project.forms import RegistrationForm, LoginForm

from flask_login import login_user, current_user, logout_user, login_required

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
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = form.password.data #bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f"Your account has been created!, You are now able to log in.", "success")
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()

		# if user and bcrypt.check_password_hash(user.password, form.password.data):
		if user and (user.password == form.password.data):
			login_user(user, remember=form.remember.data)
			return redirect(url_for('home'))

		flash('Login Unsuccessful. Please check email and password', 'danger')


	return render_template('login.html', title='Login', form=form)

@app.route("/logout")
# @login_required
def logout():
	logout_user()
	return redirect(url_for('home'))


@app.route("/profile")
@login_required
def profile():
	return render_template('profile.html', title="Profile")



@app.route("/about")
def about():
	return render_template('about.html', title='About Us')