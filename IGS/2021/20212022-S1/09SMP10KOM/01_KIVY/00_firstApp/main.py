from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class TestApp(App):

	press_count = 0

	def __init__(self):
		super().__init__()
		self.title = "Hello First App"

	def _button_press(self, button_pressed):
		# TestApp.press_count += 1;
		# print(f"Button Pressed {TestApp.press_count} time(s).")

		# input_data = self.text_input.text
		# print(input_data)

		self.text_label.text = self.text_input.text

	def _button_press1(self, button_pressed):
		self.text_label.text = self.text_input1.text

	def build(self):
		self.text_label = Label(text="Waiting for Button Press")

		button = Button(text="Click Me")
		button.bind(on_press=self._button_press)
		button1 = Button(text="Click Me")
		button1.bind(on_press=self._button_press1)


		self.text_input = TextInput(text="TextInput0")
		self.text_input1 = TextInput(text="TextInput1")

		box_layout = BoxLayout(orientation="vertical")

		box_layout_horizontal1 = BoxLayout(orientation="horizontal")
		box_layout_horizontal1.add_widget(widget=self.text_input)
		box_layout_horizontal1.add_widget(widget=button)

		box_layout_horizontal2 = BoxLayout(orientation="horizontal")
		box_layout_horizontal2.add_widget(widget=self.text_input1)
		box_layout_horizontal2.add_widget(widget=button1)

		box_layout.add_widget(widget=self.text_label)
		# box_layout.add_widget(widget=button)
		# box_layout.add_widget(widget=self.text_input)
		box_layout.add_widget(box_layout_horizontal1)
		box_layout.add_widget(box_layout_horizontal2)
		
		return box_layout

def main():
	app = TestApp()
	app.run()

if __name__ == '__main__':
	main()
