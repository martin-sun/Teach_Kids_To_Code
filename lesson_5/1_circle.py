import turtle

screen = turtle.Screen()

pen = turtle.Pen()
for i in range(8):
    pen.circle(100)
    pen.left(360/8)
screen.exitonclick() 

# pen.circle(100)
# pen.left(90)
# pen.circle(100)
# pen.left(90)
# pen.circle(100)
# pen.left(90)
# pen.circle(100)

screen.exitonclick()