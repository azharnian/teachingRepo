#https://kivy.org/doc/stable/tutorials/firstwidget.html

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Ellipse, Line


WIDTH = 9*40
HEIGHT = 16*40

Config.set('graphics', 'width', f'{WIDTH}')
Config.set('graphics', 'height', f'{HEIGHT}')
Config.write()

Window.clearcolor = get_color_from_hex('#FFFFFF')


class Painter(Widget):

	def __init__(self):
		super().__init__()
		self.line_width = 15
		self.line_color = get_color_from_hex('#0080FFFF')

	def set_line_width(self, line_width):
		self.line_width = line_width

	def set_line_color(self, line_color):
		self.line_color = line_color

	def on_touch_down(self, touch):
		# print(touch.x, touch.y)
		# print(get_color_from_hex('#0080FFFF'))
		if Widget.on_touch_down(self, touch):
			return None

		with self.canvas:
			Color(*self.line_color)
			# Ellipse(pos=(touch.x, touch.y), size=(30, 30))
			touch.ud['line'] = Line(points=(touch.x, touch.y), width=self.line_width)

	def on_touch_move(self, touch):
		# print(touch.x, touch.y)
		if 'line' in touch.ud:
			touch.ud['line'].points += [touch.x, touch.y]

	def clear_canvas(self):
		saved = self.children[:] #clone lists in different memory slot
		self.clear_widgets()
		self.canvas.clear()
		for child in saved:
			self.add_widget(child)


class PaintApp(App):

	def __init__(self):
		super().__init__()
		self.title = "Paint App"

	def build(self):
		self.paint_canvas = Painter()
		return self.paint_canvas

def main():
	app = PaintApp()
	app.run()

if __name__ == "__main__":
	main()