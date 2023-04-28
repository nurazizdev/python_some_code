from turtle import Turtle, Screen
oyna = Screen()
oyna.title('Ramka ichidagi koptok')

chiziq1 = Turtle()
chiziq1.color('green')
chiziq1.pensize(5)
chiziq1.speed(0)
chiziq1.hideturtle()
chiziq1.up()
chiziq1.goto(300, 300)
chiziq1.down()
chiziq1.goto(300, -300)
chiziq1.goto(-300, -300)
chiziq1.goto(-300, 300)
chiziq1.goto(300, 300)

chiziq2 = Turtle()
chiziq2.color('blue')
chiziq2.pensize(5)
chiziq2.speed(0)
chiziq2.hideturtle()
chiziq2.up()
chiziq2.goto(0, -260)
chiziq2.down()
chiziq2.goto(0, -300)
chiziq2.goto(-260, -300)
chiziq2.goto(-260, -260)
chiziq2.goto(0, -260)

koptok = Turtle()
koptok.shape('circle')
koptok.color('red')
koptok.up()
koptok.goto(0, 0)

step_x = 3
step_y = 2
while True:
	x, y = koptok.position()
	if x + step_x >= 300 or x + step_x <= -300:
		step_x = -step_x
	if y + step_y >= 300 or y + step_y <= -300:
		step_y = -step_y
	if -260<x<0 and -300<y<-260:
		break

	koptok.goto(x+step_x, y+step_y)


oyna.mainloop()