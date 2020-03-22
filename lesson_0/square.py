import turtle

def create_square(my_pen, forward_length):
    for x in range(4):
        my_pen.forward(forward_length)
        my_pen.left(90)


screen = turtle.Screen()
pen_1 = turtle.Pen()
pen_1.color("green")
pen_1.pensize(2)

create_square(pen_1, 100)

pen_1.color("red")

pen_1.up()
pen_1.setposition (50, -15)
pen_1.left(45)
pen_1.down()
create_square(pen_1, 100)


screen.exitonclick()    