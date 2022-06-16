#28_turtle0.py
import turtle

vito = turtle.Pen()
vito.shape("turtle")
vito.down()
#vito.color("red")
vito.speed("slowest")

"""
vito.forward(100)
vito.left(90)
vito.forward(100)
vito.left(90)
vito.forward(100)
vito.left(90)
vito.forward(100)
vito.left(90)
"""
counter_running = 0
while counter_running < 4:
	if counter_running == 0:
		vito.color("red")
	elif counter_running == 1:
		vito.color("green")
	elif counter_running == 2:
		vito.color("yellow")
	elif counter_running == 3:
		vito.color("purple")

	vito.forward(100)
	vito.left(90)
	counter_running += 1

input() #empty input to hold the program