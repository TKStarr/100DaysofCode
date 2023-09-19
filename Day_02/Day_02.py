#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("How much was the bill?\n"))
tip = float(input("How much do you want to tip?\n"))
num_people = float(input("How many people were there?\n"))

cost = (bill*(1+tip))/num_people
cost = round(float(cost), 2)
print(f"Your share is {cost}")


