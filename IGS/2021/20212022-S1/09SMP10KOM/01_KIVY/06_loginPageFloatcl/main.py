from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.core.image import Image


from kivy.utils import get_color_from_hex
from kivy.lang import Builder

LabelBase.register(name='Roboto',
					fn_regular='assets/font/Roboto-Thin.ttf',
					fn_bold='assets/font/Roboto-Medium.ttf')

Window.clearcolor = get_color_from_hex("#101216")


class MyApp(App):

	def __init__(self):
		super().__init__()
		self.title = "My Float Screen App"

		self.screen_manager = ScreenManager()
		self.screen_manager.add_widget(Builder.load_file("pages/login.kv"))
		self.screen_manager.add_widget(Builder.load_file("pages/profile.kv"))

	def logger(self):
		username_entry = self.screen_manager.screens[0].ids['username_entry'].text
		password_entry = self.screen_manager.screens[0].ids['password_entry'].text
		if username_entry == "admin" and password_entry == "admin":
			self.screen_manager.current = "profile"
		else:
			self.screen_manager.screens[0].ids['err_msg'].text = "Maaf, nama pengguna dan kata sandi tidak cocok."
		self.screen_manager.screens[0].ids['username_entry'].text = ""
		self.screen_manager.screens[0].ids['password_entry'].text = ""


	def build(self):
		self.screen_manager.current = "login"
		return self.screen_manager

if __name__ == '__main__':
	app = MyApp()
	app.run()
