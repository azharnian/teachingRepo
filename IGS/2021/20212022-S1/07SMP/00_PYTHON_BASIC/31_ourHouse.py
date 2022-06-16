import turtle
from math import sqrt


daniel = turtle.Pen()
jolin = turtle.Pen()

daniel.up()
jolin.up()

daniel.shape("turtle")
jolin.shape("turtle")
daniel.color("cyan")
jolin.color("pink")

daniel.setpos(-100,0)
jolin.setpos(100,0)

daniel.right(90) # rumah
daniel.down()
for i in range(4):
	daniel.forward(200)
	daniel.left(90)

jolin.left(90) # atap
jolin.down()

jolin.left(30)
jolin.forward(200)
jolin.left(120)
jolin.forward(200)

daniel.up()
daniel.forward(200)
daniel.left(90)
daniel.forward(67)
daniel.left(90)

daniel.down()
daniel.forward(80)
daniel.right(90)
daniel.forward(68)
daniel.right(90)
daniel.forward(80)


naren = turtle.Pen()
naren.shape("turtle")
naren.up()
naren.setpos(-67,-160)
naren.down()
naren.color("purple")
naren.circle(20)
naren.left(90)
naren.forward(2*20)
naren.right(135)
naren.up()
naren.forward(sqrt(2*20**2))
naren.right(135)
naren.down()
naren.forward(2*20)


naren.up()
naren.left(180)
naren.setpos(67,-160)
naren.down()
naren.color("purple")
naren.circle(20)
naren.left(90)
naren.forward(2*20)
naren.right(135)
naren.up()
naren.forward(sqrt(2*20**2))
naren.right(135)
naren.down()
naren.forward(2*20)


input()