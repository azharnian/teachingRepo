import json

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
		self.users = self.load_file("data/users.json")
		self.current_user = None
		self.dialog = None

		self.screen_manager = ScreenManager()
		self.screen_manager.add_widget(Builder.load_file("pages/splash.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/login.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/dashboard.kv"))

	def load_file(self, file_location):
		try:
			with open(file_location) as file:
				return json.load(file)
		except:
			return {}

	def logger(self):
		username_entry = self.root.screens[1].ids['username_entry'].text
		password_entry = self.root.screens[1].ids['password_entry'].text

		if username_entry in self.users:
			if self.users[username_entry]["password"] == password_entry:
				self.current_user = username_entry
				self.root.screens[1].ids['title'].text = ""
				self.root.screens[1].ids['username_entry'].text = ""
				self.root.screens[1].ids['password_entry'].text = ""
				self.to_dasboard()
				#print("OK")
				return True
		
		self.root.screens[1].ids['title'].text = "Login Gagal"
		self.root.screens[1].ids['username_entry'].text = ""
		self.root.screens[1].ids['password_entry'].text = ""
		#print("Not OK")
		return
		

	def build(self):
		self.screen_manager.current = "splash"
		return self.screen_manager

	def on_start(self):
		Clock.schedule_once(self.to_login_page, 3)

	def to_login_page(self, *args):
		self.screen_manager.current = "login"

	def to_dasboard(self):
		username = self.current_user
		full_name = self.users[self.current_user]["first_name"].title() + " " + self.users[self.current_user]["last_name"].title()
		bio = self.users[self.current_user]["bio"]
		profile_pic_location = "assets/img/"+self.users[self.current_user]["profile_picture"]

		self.root.screens[2].ids['label_username'].text = username
		self.root.screens[2].ids['label_fullname'].text = full_name
		self.root.screens[2].ids['label_bio'].text = bio
		self.root.screens[2].ids['profile_pic_location'].source = profile_pic_location
		self.root.current = "dashboard"

	def show_alert_dialog(self):
		if not self.dialog:
			self.dialog = MDDialog(
				title="Konfirmasi keluar",
				text="Apakah kamu yakin untuk keluar dari aplikasi?",
				#size_hint = (.8, .5),
				buttons=[
					MDFlatButton(
						text="BATAL", text_color=self.theme_cls.primary_color,
						on_release=self.close_alert_dialog
					),
					MDFlatButton(
						text="YA", text_color=self.theme_cls.primary_color,
						on_release=self.sign_out
					),
				],
			)
		self.dialog.open()

	def close_nav_drawer(self):
		self.root.screens[2].ids['nav_drawer'].set_state('close')

	def close_alert_dialog(self, *args):
		self.dialog.dismiss()
		self.close_nav_drawer()

	def sign_out(self, *args):
		self.close_alert_dialog()
		self.close_nav_drawer()
		self.current_user = None
		self.root.current = "login"



if __name__ == '__main__':
	app = MyApp()
	app.run()