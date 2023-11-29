from turtle import  Turtle,Screen


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
timmy_the_turtle.pencolor("orange")

# Draw a square with a dashed line
for direction in range (0,4):
    for dash in range(0,5):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()
    timmy_the_turtle.right(90)

timmy_the_turtle.speed(2)




screen = Screen()
screen.exitonclick()