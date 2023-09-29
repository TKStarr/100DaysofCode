# Hangman game


import random as rd
#from hangman_art import stages ##looks like this package with the ANSII art no longer exists

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = word_list[rd.randint(0,2)]
# print(chosen_word)

# Initializing variables
display = []
lives_left = 6
letters_chosen = []

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
for x in range(0,len(chosen_word)):
  display.append("_")

# Convert display list into a string for checking purposes.
display_str = ''.join(display)

# Start the game
while display_str != chosen_word and lives_left > 0:
  guess = input("Please guess a letter: ").lower()

  # Check to see if letter has already been chosen
  if guess in ''.join(letters_chosen):
    print("You have already chosen this letter, please choose another.")

  # Append the list of letters already guessed for checking in the next loop.
  letters_chosen.append(guess)

  # Check to see if the letter guessed is in the chosen word.
  for n in range(0,len(chosen_word)):
    if guess == chosen_word[n]:
      display[n] = guess

  #take away a life if it's not in the chosen word.
  if guess not in chosen_word:
    lives_left = lives_left - 1

  # Print the outputs and move onto the next guess if there are enough lives left.
  print(display)
  print(f"You have {lives_left} lives left.")
  #print(chosen_word)
  display_str = ''.join(display)

# When the while loop exits, the game is over.  This prints out the result.
if display_str == chosen_word:
  print("You win!")
else:
  print("You dead dude.")


