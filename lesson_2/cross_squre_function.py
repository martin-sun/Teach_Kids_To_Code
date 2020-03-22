import turtle

screen = turtle.Screen()

def draw_square(my_pen, side_length):
    for i in range(4):
        my_pen.forward(side_length)
        my_pen.left(90)


my_pen = turtle.Pen()
my_pen.color("blue")
my_pen.pensize(3)

my_pen.setpos(0.00,0.00)
draw_square(my_pen,100)


my_pen.up()
my_pen.setpos(50, -15.00)
my_pen.left(45)
my_pen.down()

draw_square(my_pen,100)


screen.exitonclick()
