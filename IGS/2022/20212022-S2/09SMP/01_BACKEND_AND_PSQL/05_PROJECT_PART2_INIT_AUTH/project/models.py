from flask_login import UserMixin

from project import db, login_manager

from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
	#return User.query.filter_by(id=int(user_id))
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
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