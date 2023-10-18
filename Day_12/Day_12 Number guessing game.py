import random as rd

secret_number = rd.randint(1,100)

difficulty = input("Do you want to play on easy or hard mode?")

guess_list = []

if difficulty == 'easy':
    num_guesses = 9
elif difficulty == "hard":
    num_guesses = 4
else:
    print('Please type either easy or hard.')

guess = int(input("Please guess a number"))
guess_list.append(guess)

while num_guesses > 0 and guess != secret_number:
    if guess > secret_number:
        print(f"Too high.\n You have {num_guesses} guesses remaining.")
        num_guesses = num_guesses - 1
        guess = int(input("Make a guess."))
    elif guess < secret_number:
        print(f"Too low.\n You have {num_guesses} guesses remaining.")
        num_guesses = num_guesses - 1
        guess = int(input("Make a guess."))
    else:
        print('You guessed correctly!')

    guess_list.append(guess)

if guess == secret_number:
    print(f"You got it!  The answer was {secret_number}.")
else:
    print("You're all out of guesses.  Better luck next time.")

