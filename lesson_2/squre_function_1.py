import turtle

screen = turtle.Screen()

def draw_square(my_turtle, side_length):
    for i in range(4):
        my_turtle.forward(side_length)
        my_turtle.left(90)


my_pen = turtle.Pen()
my_pen.color("blue")
my_pen.pensize(3)

my_pen.setpos(0.00,0.00)
draw_square(my_pen,70)
my_pen.up()
my_pen.setpos(-15.00, -15.00)
my_pen.down()
draw_square(my_pen,100)


screen.exitonclick()