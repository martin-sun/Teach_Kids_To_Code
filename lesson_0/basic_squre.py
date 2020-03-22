import turtle

screen = turtle.Screen()

pen = turtle.Pen()
pen.color("blue")
pen.pensize(1)

for i in range(4):
    pen.forward(100)
    pen.left(90)

screen.exitonclick()