from flask_login import UserMixin

from project import db, login_manager

from datetime import datetime

#This function for UserMixin in flask_login
@login_manager.user_loader
def load_user(user_id):
	# User.query.filter_by(id=user_id)
	return User.query.get(int(user_id))

#FLASK ORM - SQLAlchemy Object Relation Model (ORM)
class User(db.Model, UserMixin):

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True, nullable=False)
	email = db.Column(db.String(200), unique=True, nullable=False)
	image_file = db.Column(db.String(100), nullable=False, default='default.jpg')
	password = db.Column(db.String(100), nullable=False)

	tweets = db.relationship('Tweet', backref='author', lazy=True)


class Tweet(db.Model):

	id = db.Column(db.Integer, primary_key=True)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

