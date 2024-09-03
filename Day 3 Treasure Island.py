print("Welcome to Treasure Island. Your mission is to find the treasure.")

Your_Direction = input("Enter your Direction Left/Right : ").lower()

if Your_Direction == "left" :
    your_Choice = input("Enter your Choice swim/wait : ").lower()
    if your_Choice == "wait" :
        Choose_Door = input("Enter your door red/blue/yellow : ").lower()
        if Choose_Door == "yellow" :
            print("You Win")
        elif Choose_Door == "red" :
            print("Burned by fire. Game Over.")
        elif Choose_Door == "blue" :
            print("Eaten by beasts. Game Over.")
        else :
            print("Game Over")
    else :
        print("Game Over")
else :
    print("Fall into a hole. Game Over.")
