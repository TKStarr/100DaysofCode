import random as rd
from deck_of_cards import deck

dealt_cards = []
def deal_card():
    """Deals a card"""
    card = deck[rd.randint(0,51)]
    global dealt_cards

    # Makes sure the card isn't already dealt.
    while card in dealt_cards:
        card = deck[rd.randint(0, 51)]

    return card

# count = 0
# def card_count():
#     global count
#     if deck['range'][card] == 10:
#         count = count-1
#     if deck['rage'][card] < 4:
#         count = count + 1
#     else:
#         count = count + 0
#
#    return count

def calculate_score(player):
    """calculates the score"""
    score = 0
    for card in player:
        score = score + card['value']
    return score



keep_playing = input("Do you want to play a game of blackjack? (y/n)")
starting_money = int(input("How much money did you bring to gamble tonight?"))


user_wins = 0
computer_wins = 0
bet_amount = 0
total_winnings = starting_money
games_played = 0

while keep_playing == "y":
    games_played = games_played + 1
    # initial card deal
    user_cards = []
    computer_cards = []
    dealt_cards = []

    user_cards.append(deal_card())
    dealt_cards.append(user_cards[-1])
    user_cards.append(deal_card())
    dealt_cards.append(user_cards[-1])

    computer_cards.append(deal_card())
    dealt_cards.append(computer_cards[-1])
    computer_cards.append(deal_card())
    dealt_cards.append(computer_cards[-1])

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    hit = True
    bet_amount = int(input("How much would you like to bet?"))

    if bet_amount > total_winnings:
        bet_amount = int(input(f"You only have ${total_winnings} available to bet.  Please enter a number less than or equal to that amount."))

    while user_score < 21 and hit == True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        # Need to clean up this output so it doesn't print the dictionary.
        print(f"Your cards are {user_cards}")
        print(f"Your score is {user_score}")
        print(f"The dealer's first card is the {computer_cards[0]['rank']} of {computer_cards[0]['suit']}.")
        if user_score == 21:
            hit = False
            hit_or_stay = "n"

        if hit == True:
            hit_or_stay = input("Would you like to hit? (y/n)")

        if hit_or_stay == "y":
            hit = True
            user_cards.append(deal_card())
            dealt_cards.append(user_cards[-1])
            user_score = calculate_score(user_cards)
        else:
            hit = False

    # Dealer is required to keep hitting while score is below 17.
    while computer_score < 17 and user_score < 21:
        computer_cards.append(deal_card())
        dealt_cards.append(computer_cards[-1])
        computer_score = calculate_score(computer_cards)


    # Calculating winner and payout
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
    elif user_score == computer_score:
        print("Push.  No winnings or loss.")
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
    print(f"Your total winnings are ${total_winnings - starting_money}.")

    if total_winnings > 0:
        keep_playing = input("Would you like to play again? (y/n)")
    else:
        print("You're all out of money!  Better luck next time.")
        keep_playing = "n"

if total_winnings - starting_money > 0:
    print(f"Congrats!  You are walking away with ${total_winnings - starting_money}!")
elif total_winnings - starting_money == 0:
    print("Please come back soon.")
else:
    print("Better luck next time.")

