import turtle

screen = turtle.Screen()

my_pen = turtle.Pen()
my_pen.color("blue")
my_pen.pensize(3)

my_pen.setpos(0.00,0.00)
for i in range(4):
    my_pen.forward(100)
    my_pen.left(90)

my_pen.up()
my_pen.setpos(50.00, -15.00)
my_pen.left(45)
my_pen.down()

for i in range(4):
    my_pen.forward(100)
    my_pen.left(90)


screen.exitonclick()