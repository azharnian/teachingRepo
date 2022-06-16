from logger import Logger


@Logger
def display_info(name, age):
	print('display_info ran with args {} {}'.format(name, age))


display_info("devan", 17)