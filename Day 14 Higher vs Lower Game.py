from art import logo
from game_data import data
import random

def  format_data(account):
    """Format the account data into printable data"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_follower, b_follower):
    """Take the user guess and follower count and return if they got right"""
    if a_follower > b_follower :
        return guess == "a"
    else:
        return guess == "b"


#display art
print(logo)
score = 0
geme_should_continue = True
account_b = random.choice(data)

while geme_should_continue :

    #generate random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b  = random.choice(data)

    print(f"compare A : {format_data(account_a)}")
    print(f"compare A : {format_data(account_b)}")
    #Ask a user for a guess.
    guess = input("Who has a more follower? Type 'A' or 'B' : ").lower()

    #check if user is correct
    ##Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b ["follower_count"]
    Is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Score_Keeping
    if Is_correct:
        score += 1
        print(f"That's correct! and current score {score}")
    else:
        geme_should_continue = False
        print(f"sorry, That's Wrong! and Final score {score}")

