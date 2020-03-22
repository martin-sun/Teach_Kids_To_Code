import turtle

screen = turtle.Screen()
my_pen = turtle.Pen()

for x in range(100):
    my_pen.forward(x)
    my_pen.left(90)

screen.exitonclick()