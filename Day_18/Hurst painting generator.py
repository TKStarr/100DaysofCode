import random as rd
import colorgram as cg
import turtle as turt

base = int(input("How many dots going across do you want?"))
height = int(input("How many dots high do you want?"))

rgb_colors = []
colors = cg.extract("image.jpg",31)

turt.colormode(255)
t = turt.Turtle()

t.speed("fastest")
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(600)
t.setheading(0)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

# First color is background color, don't really want that.  So let's save it as bg color and then delete it from the list.
background_color = rgb_colors[0]
turt.Screen().bgcolor(background_color)
rgb_colors.pop(0)

#print(rgb_colors)

for i in range(0,height):
    for j in range(0, base):
        random_color = rd.choice(rgb_colors)
        t.dot(20,random_color)
        t.forward(50)

    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(50*base)
    t.setheading(0)

screen = turt.Screen()
screen.exitonclick()
