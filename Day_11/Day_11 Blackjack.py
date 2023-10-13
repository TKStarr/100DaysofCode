import random as rd

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# cards2 = {
#     "Ace": 11,
#     "1": 1,
#     "2": 2,
#     "3": 3,
#     "4": 4,
#     "5": 5,
#     "6": 6,
#     "7": 7,
#     "8": 8,
#     "9": 9,
#     "10": 10,
#     "Jack": 10,
#     "Queen": 10,
#     "King": 10,
# }


def deal_card():
    """Deals a card"""
    card = cards[rd.randint(0, 12)]
    return card



def calculate_score(player):
    """calculates the score"""
    count = 0
    for card in player:
        count = count + card
    return count



keep_playing = input("Do you want to play a game of blackjack? (y/n)")

user_wins = 0
computer_wins = 0
bet_amount = 0
total_winnings = 0

while keep_playing == "y":
    # initial card deal
    user_cards = []
    computer_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    hit = True
    bet_amount = int(input("How much would you like to bet?"))

    while user_score < 22 and hit == True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards are {user_cards}")
        print(f"Your score is {user_score}")
        print(f"The dealer's first card is {computer_cards[0]}.")
        if user_score == 21:
            hit = False

        if hit == True:
            hit_or_stay = input("Would you like to hit? (y/n)")

        if hit_or_stay == "y":
            hit = True
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
        else:
            hit = False

    while computer_score < 17 and user_score < 21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)



    if user_score > 21:
        print(f"Your score is {user_score}")
        print("Busted!  You lose")
        computer_wins = computer_wins + 1
        total_winnings = total_winnings - bet_amount
    elif user_score == 21:
        print(f"Your score is {user_score}")
        print("Blackjack!  Winner, winner, chicken dinner!  You win!")
        user_wins = user_wins + 1
        total_winnings = total_winnings + bet_amount
    elif computer_score > 21:
        print(f"Your score is {user_score}")
        print(f"The dealer's score is {computer_score}")
        print("You win!")
        user_wins = user_wins + 1
        total_winnings = total_winnings + bet_amount
    elif user_score >= computer_score:
        print(f"Your score is {user_score}")
        print(f"The dealer's score is {computer_score}")
        print("You win!")
        user_wins = user_wins + 1
        total_winnings = total_winnings + bet_amount
    else:
        print(f"Your score is {user_score}")
        print(f"The dealer's score is {computer_score}")
        print("You lose.")
        computer_wins = computer_wins + 1
        total_winnings = total_winnings - bet_amount


    print(f"You have won a total of {user_wins} games and the dealer has won a total of {computer_wins} games.")
    print(f"Your total winnings are ${total_winnings}.")

    keep_playing = input("Would you like to play again? (y/n)")

if total_winnings > 0:
    print(f"Congrats!  You are walking away with ${total_winnings}!")
else:
    print("Better luck next time.")

