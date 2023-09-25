import random as random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
human_pick = int(input("What do you choose? Type 0 for Rock, 1, for Paper, 2 for Scissors."))


options = [rock, paper, scissors]

comp_pick = random.randint(0,2)

human_pick_output = options[human_pick]
comp_pick_output = options[comp_pick]
print(human_pick_output)
print("Computer chose:\n" + comp_pick_output)

if human_pick == 0:
  if comp_pick == 1:
    print("You win!")
  elif comp_pick == 2:
    print("You lose.")
  else:
    print("It's a tie.")
elif human_pick == 1:
  if comp_pick == 1:
    print("It's a tie.")
  elif comp_pick == 2:
    print("You lose.")
  else:
    print("You Win!")
else:
  if comp_pick == 1:
    print("You lose.")
  elif comp_pick == 2:
    print("It's a tie")
  else:
    print("You Win!")
