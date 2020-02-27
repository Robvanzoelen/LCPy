import turtle

screen = turtle.Screen()
leonardo = turtle.Turtle()

for counter in range(250):
    if counter % 2 == 0:
        leonardo.forward(counter*5)
    else:
        leonardo.right(25)
        leonardo.forward(counter*3)
    leonardo.left(75)

screen.exitonclick()

