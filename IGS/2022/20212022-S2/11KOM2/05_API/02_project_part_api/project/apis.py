from project import db, api
from project.models import User
from project.forms import LoginForm, RegistrationForm

from flask import jsonify
from flask_restful import Resource
from flask_login import login_user, current_user, logout_user, login_required

class LoginAPI(Resource):

	def post(self):
		form = LoginForm()
		user = User.query.filter_by(email=form.email.data).first()

		if user and (user.password == form.password.data):
			login_user(user)
			return jsonify({
				"success" : True,
				"profile" : {
					"username" : current_user.username,
					"user_id" : current_user.id
					}
				})
		return jsonify({
			"success" : False,
			"message" : "Login Failed"
			})

class LogoutAPI(Resource):
	def get(self):
		if current_user.is_authenticated:
			logout_user()
			return jsonify({
				"success" : True,
				"message" : "User has been logout."
				})
		return jsonify({
			"success" : False,
			"message" : "No need to logout."
			})

class UserAPI(Resource):

	@login_required
	def get(self, username):

		user = User.query.filter_by(username=username).first()

		if user is None:
			return jsonify({
				'success' : False
				})

		return jsonify({
			'id' : user.id,
			'username' : user.username,
			'email' : user.email,
			'image_file' : user.image_file
			})

api.add_resource(LoginAPI, "/api/user/login", methods=["POST"])
api.add_resource(LogoutAPI, "/api/user/logout")
api.add_resource(UserAPI, "/api/user/<string:username>", methods=["GET"])

