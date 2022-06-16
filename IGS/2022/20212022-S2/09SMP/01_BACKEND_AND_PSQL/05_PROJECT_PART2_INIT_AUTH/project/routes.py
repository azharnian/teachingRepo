import os
import secrets
from PIL import Image #Pillow

from flask import render_template, url_for, redirect, flash
from flask_login import login_user, current_user, logout_user, login_required

from werkzeug.security import generate_password_hash, check_password_hash

from project import app, db#, bcrypt
from project.forms import RegistrationForm, LoginForm, UpdateProfileForm
from project.models import User, Tweet

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
		# hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
		hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=16)
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f"Account created for {form.username.data}!", "success")
		return redirect(url_for('login'))

	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		# user = User.query.filter_by(username=form.username.data).first()
		user = User.query.filter(User.username == form.username.data).first()
		if user and check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			flash('Login Success', 'info')
			return redirect(url_for('home'))
		flash('Login Failed, please check your username and password', 'danger')

	return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route("/about")
def about():
	return render_template('about.html', title='About Us')


def save_picture(form_picture):
	file_name, file_ext = os.path.splitext(form_picture.filename)
	random_name = secrets.token_hex(16)
	picture_name = random_name+file_ext

	piture_path = os.path.join(app.root_path, 'static/profile_pictures', picture_name)

	image = Image.open(form_picture)
	image.thumbnail((125, 125))
	image.save(piture_path)

	return picture_name



@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
	form = UpdateProfileForm()

	if form.validate_on_submit():

		current_user.username = form.username.data
		current_user.email = form.email.data

		if form.picture.data:
			picture_file = save_picture(form.picture.data)
			current_user.image_file = picture_file

		db.session.commit()
		flash('Your account has been updated!', 'success')


	image_file = url_for('static', filename='profile_pictures/'+current_user.image_file)

	form.username.data = current_user.username
	form.email.data = current_user.email
	return render_template('profile.html', title="Profile", image_file=image_file, form=form)







