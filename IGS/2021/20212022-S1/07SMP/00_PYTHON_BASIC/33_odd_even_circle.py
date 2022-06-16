import turtle

viena = turtle.Pen()
# viena.shape("classic")
viena.up()
viena.speed(0)
viena.setpos(-300,0)

number = 0
while number < 10:
	viena.down()
	if number % 3 == 0:
		viena.color("red")
		viena.fillcolor("red")
	elif number % 3 == 1:
		viena.color("yellow")
		viena.fillcolor("yellow")
	else:
		viena.color("green")
		viena.fillcolor("green")
	viena.begin_fill()
	viena.circle(100)
	viena.end_fill()
	viena.up()
	viena.forward(50)
	number += 1


input()