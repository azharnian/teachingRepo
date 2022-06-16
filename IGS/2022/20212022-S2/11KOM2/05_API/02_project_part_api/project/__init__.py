from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_restful import Api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e463a74a1f16cfff3c0b64881fc4a56f'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# bcrypt = Bcrypt(app) 
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

api = Api(app)

from project import apis
from project import routes