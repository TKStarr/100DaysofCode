import random as rd
import turtle
from turtle import  Turtle,Screen


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")

shapes = range(0,50)
turtle.colormode(255)
timmy_the_turtle.width(4)

for shape in shapes:
    red = rd.randint(0, 255)
    green = rd.randint(0, 255)
    blue = rd.randint(0, 255)
    timmy_the_turtle.pencolor((red,green,blue))
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(360/len(shapes))


timmy_the_turtle.speed(2)




screen = Screen()
screen.exitonclick()