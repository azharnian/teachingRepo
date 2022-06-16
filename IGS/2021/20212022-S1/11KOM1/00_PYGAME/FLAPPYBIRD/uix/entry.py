import pygame

from uix.button import Button

class Entry(Button):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.text = ""
		self.active = False
		self.font_file = self.my_settings.ENTRY_FONT
		self.color = self.my_settings.ENTRY_COLOR_INACTIVE

	def update(self):
		self.text_to_image(self.text)
