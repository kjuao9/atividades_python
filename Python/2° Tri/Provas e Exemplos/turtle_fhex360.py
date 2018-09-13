import turtle
b = turtle.Turtle()
lados = 11
angulo = 360/ lados
for x in range(lados):
	b.forward(100)
	b.left(angulo)
