# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

# Write your code below this row 👇

sum_height = 0
for height in student_heights:
   sum_height = sum_height + height
   print(f"total height = {sum_height}")

num_students = 0
for student in student_heights:
   num_students = num_students +1
   print(f"Number of students = {num_students}")

avg_height = round(sum_height / num_students)
print(avg_height)

