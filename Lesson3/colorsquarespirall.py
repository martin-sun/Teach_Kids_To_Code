import turtle

screen = turtle.Screen()

my_pen = turtle.Pen()

my_color = ["red", "blue", "green", "Yellow"]

for x in range(100):
    print(x%len(my_color))
    my_pen.pencolor(my_color[x%len(my_color)])
    my_pen.forward(x)
    my_pen.left(90)


screen.exitonclick()