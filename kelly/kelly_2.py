import turtle
screen = turtle.Screen()
screen.bgcolor("green")

pen = turtle.Pen()
pen.pencolor("blue")
pen.shape("turtle")
pen.pensize(5)
for i in range (12):
    pen.penup()
    pen.forward(100)
    pen.down()
    pen.forward(30)
    pen.penup()
    pen.forward(20)
    pen.down()
    pen.stamp()
    pen.penup()
    pen.backward(150)
    pen.left(360/12)

screen.exitonclick()