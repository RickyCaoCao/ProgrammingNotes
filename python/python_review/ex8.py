# Exercise 8 - Rock Paper Scissors
# Uncompleted because not challenging

import random as rand

while(1):
    print("Welcome to Rock, Paper, Scissors")
    user_in = raw_input("Enter 'rock', 'paper', or 'scissors': ")    

    if user_in == "rock":
        pos = 2
    elif user_in == "paper":
        pos = 1
    elif user_in == "scissors":
        pos = 0
    else:
        print("You entered an invalid position.")
        break
    
    comp_pos = ["scissors", "paper", "rock"]
    outcome = rand.randint(-1, 1)
    outcome_s = ["lose", "tied", "win"][outcome+1]

    print("You played {}!".format(user_in))
    print("The computers plays {}!".format(comp_pos[(pos + outcome)%3]))
    print("You {}.".format(outcome_s))

    replay = raw_input("enter y to play again: ")
    if replay != 'y':
        break