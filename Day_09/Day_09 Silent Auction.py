from replit import clear

# create list of bids
bid_list = []

# create function to create a dictionary for each new bidder, then add it to the list of bids.
def add_new_bid(bidder, bid_amount):
    bid = {}
    bid["bidder"] = bidder
    bid["amount"] = bid_amount
    bid_list.append(bid)

others_check = "yes"

# loop to fill list with dictionaries of entrants
while others_check == "yes":
    name = input("What is your name?: ")
    bid_amt = int(input("How much do you want to bid?: "))
    others_check = input("Are there any other bidders?: ")
    add_new_bid(name, bid_amt)
    clear()

# filter out a dictionary which only contains the details of the winner.
max_bid_dict = max(bid_list, key=lambda x:x['amount'])
winning_bid_amount = max_bid_dict['amount']
winning_bidder = max_bid_dict['bidder']

# print winning bidder
print(f'The winner is {winning_bidder} with a bid of ${winning_bid_amount}!')