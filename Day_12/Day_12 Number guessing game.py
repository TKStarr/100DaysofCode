import random as rd

secret_number = rd.randint(1,100)

difficulty = input("Do you want to play on easy or hard mode?")

guesses_list = []

if difficulty == 'easy':
    num_guesses = 10
elif difficulty == "hard":
    num_guesses = 5
else:
    print('Please type either easy or hard.')


guess = 0

while num_guesses > 0 and guess != secret_number:
    guess = int(input("Please guess a number"))
    guesses_list.append(guess)
    if guess > secret_number:
        print(f"Too high.\n You have {num_guesses - 1} guesses remaining.")
        num_guesses = num_guesses - 1
    elif guess < secret_number:
        print(f"Too low.\n You have {num_guesses - 1} guesses remaining.")
        num_guesses = num_guesses - 1
    else:
        print('You guessed correctly!')




if guess == secret_number:
    print(f"You got it!  The answer was {secret_number}.")
else:
    print("You're all out of guesses.  Better luck next time.")

