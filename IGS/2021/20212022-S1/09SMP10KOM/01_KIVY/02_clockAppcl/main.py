from datetime import datetime

# cython , kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

from kivy.core.text import LabelBase

LabelBase.register(name="Roboto",
					fn_regular="Roboto-Thin.ttf",
					fn_bold="Roboto-Medium.ttf")

class ClockApp(App):

	def __init__(self):
		super().__init__()
		self.title = "Clock App"

		self.stopwatch_started = False

	def update_clock(self, *args):
		time = datetime.now()
		#print(args)
		#type(time)
		self.root.ids['time'].text = time.strftime("[b]%H[/b]:%M:%S")
		self.update_stopwatch()

	def update_stopwatch(self):
		if self.stopwatch_started:
			time = datetime.now() - self.stopwatch_time_start
			time = str(time)[0:10]
			# print(time)
			self.root.ids['stopwatch'].text = f"{time[2:8]}[size=40]{time[8:10]}[/size]"


	def start_stop(self):
		text = "Start"
		if not self.stopwatch_started:
			self.stopwatch_time_start = datetime.now()
			text = "Stop"
		self.root.ids['start_stop'].text = text
		self.stopwatch_started = not self.stopwatch_started


	def reset(self):
		if self.stopwatch_started:
			self.root.ids['start_stop'].text = 'Start'
			self.stopwatch_started = False
		self.root.ids['stopwatch'].text = "00:00.[size=40]00[/size]"

	def on_start(self):
		clock_trigger = Clock.schedule_interval(self.update_clock, 1/60)

	def build(self):
		return Builder.load_file("page.kv")

def main():
	app = ClockApp()
	app.run()

if __name__ == '__main__':
	main()