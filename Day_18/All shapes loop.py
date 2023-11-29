import random as rd
import turtle
from turtle import  Turtle,Screen


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")

shapes = range(3,11)
turtle.colormode(255)

for shape in shapes:
    red = rd.randint(0, 255)
    green = rd.randint(0, 255)
    blue = rd.randint(0, 255)
    timmy_the_turtle.pencolor((red,green,blue))
    angle = 180*(shape - 2)/shape
    for line in range(0,shape):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.left(180 - angle)




timmy_the_turtle.speed(2)




screen = Screen()
screen.exitonclick()