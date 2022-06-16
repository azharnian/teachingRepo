#https://kivy.org/doc/stable/tutorials/firstwidget.html
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.core.text import LabelBase
from kivy.config import Config
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.togglebutton import ToggleButton

from settings import Settings

Config.set('graphics', 'width', f'{Settings.SCREEN_WIDTH}')
Config.set('graphics', 'height', f'{Settings.SCREEN_HEIGHT}')
Config.set('graphics', 'resizable', '0')
Config.set('input', 'mouse', 'mouse, disable_multitouch')
Config.write()

Window.clearcolor = get_color_from_hex('#FFFFFF')


class PainterWidget(Widget):

	def __init__(self):
		super().__init__()
		self.line_width = 10
		self.line_color = get_color_from_hex('#0080FFFF')

	def on_touch_down(self, touch):
		if Widget.on_touch_down(self, touch):
			return
		# print(touch)
		with self.canvas:
			self.color = Color(*self.line_color)
			# d = 30.
			# print(self.color)
			#Ellipse(pos=(touch.x-d/2, touch.y-d/2), size=(d,d))
			touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_width)
			#Line(circle=(touch.x, touch.y, 25), width=4)

	def on_touch_move(self, touch):
		if 'line' in touch.ud:
			touch.ud['line'].points += [touch.x, touch.y]

	def clear_canvas(self):
		saved = self.children[:]
		self.clear_widgets()
		self.canvas.clear()
		for widget in saved:
			self.add_widget(widget)

	def set_line_width(self, line_width):
		self.line_width = int(line_width)

	def set_color_line(self, background_color):
		# print(hex_code)
		# self.last_color = hex_code
		# self.canvas.add(Color(*hex_code))
		# print(self.canvas.__str__)
		self.line_color = background_color


class PaintApp(App):

	def __init__(self):
		super().__init__()
		self.title = 'Paint App'


	def build(self):
		self.paint_app = PainterWidget()
		return self.paint_app

def main():
	app = PaintApp()
	app.run()

if __name__ == '__main__':
	main()