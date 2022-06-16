import json
import bcrypt

from settings import Settings
from models.user import User

from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from kivy.core.text import LabelBase
from kivy.core.window import Window

from kivy.config import Config

from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang import Builder


LabelBase.register(name='Roboto',
					fn_regular='assets/font/Roboto-Thin.ttf',
					fn_bold='assets/font/Roboto-Medium.ttf')

WIDTH = 9*40
HEIGHT = 16*40

Config.set('graphics', 'width', f'{WIDTH}')
Config.set('graphics', 'height', f'{HEIGHT}')
Config.write()

Window.clearcolor = get_color_from_hex("#101216")

class MyApp(MDApp):

	def __init__(self):
		super().__init__()
		self.title = "My KIVY MD APP"
		self.settings = Settings()
		# self.users = self.load_data("data/users.json")
		self.current_user = None
		self.dialog_box = None

		self.screen_manager = ScreenManager()
		self.screen_manager.add_widget(Builder.load_file("pages/splash.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/login.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/dashboard.kv"))

	def load_data(self, file_location):
		try:
			with open(file_location) as file:
				return json.load(file)
		except:
			return {}

	def find_user_by_username(self, username):
		with self.settings.conn:
			self.settings.cur.execute(""" 
				SELECT * FROM users WHERE username=:username
				""",{"username" : username})
		return self.settings.cur.fetchone()

	def logger(self):
		username_entry = self.root.screens[1].ids['username_entry'].text
		password_entry = self.root.screens[1].ids['password_entry'].text

		user = self.find_user_by_username(username_entry)

		if user:
			if bcrypt.checkpw(password_entry.encode("utf-8"), user[2]):
				self.root.screens[1].ids['msg'].text = ""
				self.root.screens[1].ids['username_entry'].text = ""
				self.root.screens[1].ids['password_entry'].text = ""

				self.current_user = User(user[1], user[3], user[4])
				self.current_user.id = user[0]
				self.current_user.bio = user[5]
				self.current_user.interest = user[6]
				self.current_user.pic = user[7]
				self.to_dashboard()
				return True

		self.root.screens[1].ids['msg'].text = "Login Gagal"
		self.root.screens[1].ids['username_entry'].text = ""
		self.root.screens[1].ids['password_entry'].text = ""


	def build(self):
		self.screen_manager.current = "login"
		return self.screen_manager

	#def on_start(self):
	#	Clock.schedule_once(self.to_login_page, 3)

	def to_login_page(self, *args):
		self.screen_manager.current = "login"

	def to_dashboard(self):
		fullname = self.current_user.first.title()+" "+self.current_user.last.title()
		bio = self.current_user.bio
		pic = "assets/img/"+self.current_user.pic

		self.root.screens[2].ids['label_username'].text = self.current_user.username
		self.root.screens[2].ids['label_fullname'].text = fullname
		self.root.screens[2].ids['label_bio'].text = bio
		self.root.screens[2].ids['profile_pic'].source = pic
		self.root.current = "dashboard"

	def close_dialog(self, *args):
		self.dialog_box.dismiss()
		self.root.screens[2].ids['nav_drawer'].set_state('close')

	def exit(self, *args):
		self.close_dialog()
		self.current_user = None
		self.root.current = "login"

	def sign_out(self, *args):
		if not self.dialog_box:
			self.dialog_box = MDDialog(
				title="Konfirmasi Keluar",
				text="Apakah yakin keluar dari aplikasi ?",
				buttons=[
					MDFlatButton(
						text="Batal",
						on_release = self.close_dialog
						),
					MDFlatButton(
						text="Ya",
						on_release = self.exit
						)
				]
				)
		self.dialog_box.open()



if __name__ == '__main__':
	app = MyApp()
	app.run()