
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.utils import get_color_from_hex
from kivy.lang import Builder

LabelBase.register( name='Roboto',
                    fn_regular='Roboto-Thin.ttf',
                    fn_bold='Roboto-Medium.ttf')

Window.clearcolor = get_color_from_hex('#101216')

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.title = "My App with Screens"


    def auth(self):
        username_entry = self.root.screens[0].ids['username_entry'].text
        password_entry = self.root.screens[0].ids['password_entry'].text
        if username_entry == "admin" and password_entry == "12345":
            self.root.current = 'HomeScreen'
        else:
            self.root.screens[0].ids['error_message'].text = "Maaf, Nama Pengguna dan Kata Sandi tidak cocok."
        self.root.screens[0].ids['username_entry'].text = ""
        self.root.screens[0].ids['password_entry'].text = ""

    def build(self):
        return Builder.load_file("index.kv")

if __name__ == '__main__':
    app = MyApp()
    app.run()