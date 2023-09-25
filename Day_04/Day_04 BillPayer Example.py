# Import the random module here
import random as random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(names[1])
len_names = len(names)
billpayer_no = random.randint(0, len_names - 1)
billpayer_name = names[billpayer_no]
print(f"{billpayer_name} is going to buy the meal today!")
