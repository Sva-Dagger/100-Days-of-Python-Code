# 100-Days-of-Python-Code
Day 1 to 100 Days of Python Coding

Day 1 Project Band-Name-Generator

    print("Welcome to Band name Generator")
    city = input("Enter your city ")          
    Pet = input("What's your pet name ") 
    print("Your band name could be " + city + " " + Pet)

Day 2 Project - Tip-Calculator

    Total_bill = float(input("Enter your total bill in $ "))
    Tip_in_percent = (float(input("Enter your Tip in % "))/100)
    Sharing_persons = int(input("Enter total number of sharing persons "))
    
    Tip = (Total_bill*Tip_in_percent)
    bill_with_Tip = Total_bill + Tip
    Total_Shared_Bill = (round(bill_with_Tip/Sharing_persons, 2))
    
    print(f"Each Person Should Pay {Total_Shared_Bill}$")

Day 3 Project - Treasure Island

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

Day 4 Project - Treasure Map

    line1 = ["⬜️","️⬜️","️⬜️"]
    line2 = ["⬜️","⬜️","️⬜️"]
    line3 = ["⬜️️","⬜️️","⬜️️"]
    map = [line1, line2, line3]
    print("Hiding your treasure! X marks the spot.")
    position = input() # Where do you want to put the treasure?
    letter = position[0].lower()
    abc = ["a", "b", "c"]
    letter_index = abc.index(letter)
    number_index = int(position[1])-1
    map[number_index][letter_index] = "X"
    print(f"{line1}\n{line2}\n{line3}")

Day 5 Project - Password generator (Easy)

    #Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    
    #Easy_Level
    password =  ""
    
    for char in range (1, nr_letters+1):
      password += random.choice(letters)
    for char in range (1, nr_symbols+1):
      password += random.choice(symbols)
    for char in range (1, nr_numbers+1):
      password += random.choice(numbers)
    print(password)

Day 5 Project - Password generator (Hard)

    #Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    #Hard_Level
    
    password_list = []
    
    for char in range (1, nr_letters+1):
      password_list += random.choice(letters)
    for char in range (1, nr_symbols+1):
      password_list += random.choice(symbols)
    for char in range (1, nr_numbers+1):
      password_list += random.choice(numbers)
    random.shuffle(password_list)
    
    password = ""
    for char in password_list :
      password += char
    print(password)
    
