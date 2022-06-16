from kivymd.app import MDApp

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.text import LabelBase
from kivy.core.window import Window

from kivy.clock import Clock
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

LabelBase.register( name="Roboto", fn_regular="Roboto-Thin.ttf", fn_bold="Roboto-Medium.ttf")
Window.clearcolor = get_color_from_hex("#101216")


class TestApp(MDApp):

	def __init__(self):
		super().__init__()
		self.title = "Test MD App"
		self.screen_manager = ScreenManager()
		self.screen_manager.add_widget(Builder.load_file("splash.kv"))
		self.screen_manager.add_widget(Builder.load_file("login.kv"))

	def build(self):
		self.screen_manager.current = "splash"
		return self.screen_manager

	def on_start(self):
		Clock.schedule_once(self.start_login, 3)

	def start_login(self, *args):
		self.screen_manager.current = "login"


if __name__ == '__main__':
	app = TestApp()
	app.run()
