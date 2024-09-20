from random import randint
Easy_Level_Turns = 10
Hard_Level_Turns = 5

#Functions to check user's guess against actual answer
turns = 0
def check_answer(guess, answer, turns):
    """Check answer against guess. Returns the no of turns remaining."""
    if guess > answer :
        print("Too High")
        return turns - 1
    elif guess < answer :
        print("Too Low")
        return turns - 1
    else :
        print(f"You got it! The actual answer is {answer}")

#Make function to set difficulty
def Set_Difficulty():
    level = input("Choose the Difficulty. Type 'easy' or 'hard' : ")
    if level == "easy" :
        return Easy_Level_Turns
    else:
        return Hard_Level_Turns

#Choosing random number from 1 to 100
print("Welcome to the Number Guessing Game")
print("I'm thinking of number from 1 to 100")
answer = randint(1, 100)
print(f"psst, the actual answer is {answer}")

#Let the user guess the number
turns = Set_Difficulty()

guess = 0
Is_game_over = True
while guess != answer or not Is_game_over:
    print(f"You have {turns} attempts remaining to guess the numer.")
    guess = int(input("Make the guess : "))
    turns = check_answer(guess, answer, turns)

    if turns == 0 :
        print("You have ran out of chance. You lose.")
        Is_game_over = True
    elif guess != answer :
        print("guess again.")



#Fuunction to check user's guess against actual answer

#Track the number of turns and reduce by 1 if they get it wrong

#Repeat the guessing functionality if they get it wrong

