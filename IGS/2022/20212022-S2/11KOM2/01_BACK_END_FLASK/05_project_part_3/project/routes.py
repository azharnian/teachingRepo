from flask import render_template, url_for, redirect, flash, request, abort

from project import app, db #,bcrypt
from project.models import User, Tweet
from project.forms import RegistrationForm, LoginForm, UpdateProfileForm, TweetForm

from flask_login import login_user, current_user, logout_user, login_required


@app.route("/", methods=['GET', 'POST']) # 127.0.0.1:8000
@app.route("/home", methods=['GET', 'POST']) # 127.0.0.1:8000/home
def home():
	form = TweetForm()

	if form.validate_on_submit() and current_user.is_authenticated :
		tweet = Tweet(content=form.content.data, user_id=current_user.id)
		db.session.add(tweet)
		db.session.commit()
		flash('Your tweet has been created!', 'success')
		return redirect(url_for('home'))

	# tweets = Tweet.query.order_by(Tweet.date_posted.desc()).all()
	tweets = Tweet.query.order_by(Tweet.date_posted.desc()).paginate(per_page=5)

	last_page = list(tweets.iter_pages())[-1]

	return render_template('home.html', tweets=tweets, form=form, last_page=last_page)

@app.route("/register", methods=['GET', 'POST'])
def register():
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
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()

		# if user and bcrypt.check_password_hash(user.password, form.password.data):
		if user and (user.password == form.password.data):
			login_user(user, remember=form.remember.data)
			return redirect(url_for('profile'))

		flash('Login Unsuccessful. Please check email and password', 'danger')
	return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

import secrets
import os
from PIL import Image

def save_data(form_picture):
	#file name and path
	random_file_name = secrets.token_hex(16)
	f_name, f_ext = os.path.splitext(form_picture.filename)
	picture_file_name = random_file_name + f_ext
	picture_file_path = os.path.join(app.root_path, 'static/profile_pictures', picture_file_name)

	#image compress processing
	output_size = (125, 125)
	image = Image.open(form_picture)
	image.thumbnail(output_size)
	image.save(picture_file_path)

	return picture_file_name

@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
	form = UpdateProfileForm()
	if form.validate_on_submit():

		if form.picture.data:
			current_user.image_file = save_data(form.picture.data)
		current_user.username = form.username.data
		db.session.commit()
		flash("Your account has been updated!", "success")
		return redirect(url_for('profile'))

	elif request.method == 'GET':
		form.username.data = current_user.username
	image_file = url_for('static', filename='profile_pictures/'+current_user.image_file)
	return render_template('profile.html', title="Profile", image_file=image_file, form=form)

@app.route("/about")
def about():
	return render_template('about.html', title='About Us')


@app.route("/tweet/<int:tweet_id>", methods=["GET", "POST"])
@login_required
def tweet(tweet_id):

	tweet = Tweet.query.get_or_404(tweet_id)

	if tweet.author != current_user:
		abort(403) #forbidden

	form = TweetForm()

	if form.validate_on_submit():
		tweet.content = form.content.data
		db.session.commit()
		flash('Your tweet has been updated!', 'success')
		return redirect(url_for('home'))

	form.content.data = tweet.content
	return render_template('tweet.html', title='Tweet', form=form, tweet=tweet)

@app.errorhandler(404)
def error_404(error):
	return render_template('errors/404.html'), 404

@app.errorhandler(403)
def error_403(error):
	return render_template('errors/403.html'), 403

@app.errorhandler(500)
def error_500(error):
	return render_template('errors/500.html'), 500













