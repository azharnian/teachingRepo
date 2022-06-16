from datetime import datetime

from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

from kivy.lang import Builder



LabelBase.register(	name='Roboto',
					fn_regular='Roboto-Thin.ttf',
					fn_bold='Roboto-Medium.ttf')

Window.clearcolor = get_color_from_hex('#101216')


class ClockApp(App):


	def __init__(self):
		super().__init__()
		self.title = "Clock App"
		self.stopwatch_started = False

	def update_time(self, interval):
		time = datetime.now()
		self.root.ids['time'].text = time.strftime("[b]%H[/b]:%M:%S")
		self.update_stopwatch(interval)

	def update_stopwatch(self, interval):
		if self.stopwatch_started:
			time = str((datetime.now() - self.time_sw_started))
			time = datetime.strptime(time, '%H:%M:%S.%f')
			time = time.strftime("%M:%S.%f")
			self.root.ids['stopwatch'].text = f"{time[0:6]}[size=40]{time[6:8]}[/size]"

	def reset(self):
		if self.stopwatch_started:
			self.root.ids['start_stop'].text = 'Start'
			self.stopwatch_started = False
		self.root.ids['stopwatch'].text = "00:00.[size=40]00[/size]"

	def start_stop(self):
		text = 'Start'
		if not self.stopwatch_started:
			text = 'Stop'
		self.root.ids['start_stop'].text = text
		self.stopwatch_started = not self.stopwatch_started
		self.time_sw_started = datetime.now()

	def on_start(self):
		Clock.schedule_interval(self.update_time, 0)

	def build(self):
		return Builder.load_file('index.kv')

def main():
	app = ClockApp()
	app.run()

if __name__ == '__main__':
	main()