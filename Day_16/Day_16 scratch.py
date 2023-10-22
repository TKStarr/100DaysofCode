import turtle
import turtle as trt
from prettytable import PrettyTable as pt

# Franklin = trt.Turtle()
#
# print(Franklin)
# Franklin.shape("turtle")
# Franklin.color("blue")
# Franklin.forward(100)
#
# my_screen = trt.Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()
# #turtle.done()

table = pt()
table.add_column("Pokemon Name",["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"

print(table)
