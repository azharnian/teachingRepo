from datetime import datetime

import logging

def logger(original_function):

	logging.basicConfig(filename='app.log', level=logging.INFO)

	def wrapper(*args, **kwargs):

		logging.info(f'{datetime.now()} : {original_function.__name__} - ARGS : {args} KWARGS : {kwargs}')

		return original_function(*args, **kwargs)

	return wrapper


@logger
def display_info(name, age):
	print('display_info ran with args {} {}'.format(name, age))


display_info("devan", 17)