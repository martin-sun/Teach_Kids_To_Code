import turtle

window = turtle.Screen()
window.bgcolor("green")

pen = turtle.Pen()
pen.pencolor("blue")
pen.pensize(5)
pen.shape("turtle")

def draw_clock():
    pen.penup()
    pen.forward(150)
    pen.pendown()
    pen.forward(30)
    pen.penup()
    pen.forward(30)
    pen.stamp()
    pen.backward(210)

for i in range(12):
    draw_clock()
    pen.left(360/12)


window.exitonclick()