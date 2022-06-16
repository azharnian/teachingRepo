from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm, LoginForm

from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f10b0e18ba733700d98d19e876f79caab719d8eda3502cf3d46543f780cbad45'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(256), unique=True, nullable=False)
	email = db.Column(db.String(256), unique=True, nullable=False)
	password = db.Column(db.String(256), nullable=False)
	date_signed_up = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	date_updated = db.Column(db.DateTime)
	email_verified = db.Column(db.Boolean, nullable=False, default=False)
	image_file = db.Column(db.String(256), nullable=False, default='default.jpg')

	tweets = db.relationship('Tweet', backref='creator', lazy=True)
	# tweet.creator.username

	def __repr__(self):
		return f"User({self.username} - {self.email} - {self.date_signed_up} )"

class Tweet(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text, nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	replies = db.relationship('Reply', backref='replied_to_tweet', lazy=True)
	likes = db.relationship('Like', backref='liked_to_tweet', lazy=True)
	# reply.replied_to_tweet.content

class Reply(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text, nullable=False)
	date_replied = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	tweet_id = db.Column(db.Integer, db.ForeignKey('tweet.id'), nullable=False)

class Like(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date_liked = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	tweet_id = db.Column(db.Integer, db.ForeignKey('tweet.id'), nullable=False)

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





