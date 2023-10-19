import random

suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

deck = []

for suit in suits:
    for rank, value in zip(ranks, values):
        card = {"suit": suit, "rank": rank, "value": value}
        deck.append(card)

random.shuffle(deck)