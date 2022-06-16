from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

#class object dari uis disebut widget

class MyFirstApp(App):

	def __init__(self):
		super().__init__()
		self.title = "First Kivy App"

	def build(self):

		title_label = Label(text="Waiting for Button Press")
		boxlayout1 = BoxLayout(orientation="horizontal")
		entry1 = TextInput(text="Entry 1")
		button1 = Button(text="Click Me")
		boxlayout1.add_widget(entry1)
		boxlayout1.add_widget(button1)

		boxlayout2 = BoxLayout(orientation="horizontal")
		entry2 = TextInput(text="Entry 2")
		button2 = Button(text="Click Me")
		boxlayout2.add_widget(entry2)
		boxlayout2.add_widget(button2)
		

		main_boxlayout = BoxLayout(orientation="vertical")
		main_boxlayout.add_widget(title_label)
		main_boxlayout.add_widget(boxlayout1)
		main_boxlayout.add_widget(boxlayout2)
		return main_boxlayout

if __name__ == "__main__":
	app = MyFirstApp()
	app.run()