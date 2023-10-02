# Write your code below this line 👇
import math


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.
def paint_calc(height, width, cover):
  num_cans = height * width / cover
  num_cans = math.ceil(num_cans)
  print(f"You need {num_cans} cans of paint.")


# 🚨 Don't change the code below 👇
test_h = int(input("How high is the wall? \n")) # Height of wall (m)
test_w = int(input("How wide is the wall? \n")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

