import turtle

screen = turtle.Screen()

pen = turtle.Pen()

for x in range(30):
    pen.circle(100)
    pen.left(360/30)

screen.exitonclick()