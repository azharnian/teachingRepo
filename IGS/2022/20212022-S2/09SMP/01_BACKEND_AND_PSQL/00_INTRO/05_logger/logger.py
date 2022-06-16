from datetime import datetime
import logging

class Logger:

	def __init__(self, original_function):
		logging.basicConfig(filename='app.log', level=logging.INFO)
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		logging.info(f'{datetime.now()} : {self.original_function.__name__} - ARGS : {args} KWARGS : {kwargs}')
		return self.original_function(*args, **kwargs)