import art
import game_data as gd
import random as rd

print(art.logo)

score = 0
count_wrong = 0
try_again = 'y'
final_scores = []


while try_again == 'y':
    while count_wrong == 0:
        A = gd.data[rd.randint(0, 49)]
        B = gd.data[rd.randint(0, 49)]
        # TODO make sure that A and B aren't the same

        A_followers = A['follower_count']
        B_followers = B['follower_count']

        if A_followers > B_followers:
            answer = 'A'
        else:
            answer = 'B'


        print(f'Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}')
        print(art.vs)
        print(f'Against B: {B["name"]}, a {B["description"]}, from {B["country"]}')

        guess = input("Do you think A or B has more followers?  Type \'A\' or \'B\'")

        if guess == answer:
            print(f'Congrats!  {A["name"]} has {A_followers} million followers and {B["name"]} has {B_followers} million followers.\n \n')
            score = score + 1
        else:
            print(f'Wrong answer.  {A["name"]} has {A_followers} million followers and {B["name"]} has {B_followers} million followers.\n \n')
            count_wrong = 1

    print(f'Your final score is {score}.')
    final_scores.append(score)
    try_again = input('Do you want to play again? (y/n)')

    if try_again == 'y':
        count_wrong = 0
    else:
        print(f"Your highest score is {max(final_scores)}")