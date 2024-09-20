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

Day 6 Project - Picking random word

    Word_List = ["Apple", "Ball", "Cat", "Banana"]
    
    import random
    
    Choosen_word = random.choice(Word_List)
    print(Choosen_word)
    
    guess = input("Guess your word: ").lower()
    
    for letter in Choosen_word :
      if letter == guess :
        print("right")
      else :
        print("Wrong")

Day 7 Project - Hang Man

    import random
    
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']
    
    Word_List = ["apple", "ball", "cat", "banana"]
    
    Choosen_word = random.choice(Word_List)
    print(Choosen_word)
    word_legth = len(Choosen_word)
    new_list = []
    for _ in range(word_legth) :
      new_list += "_"
    print(new_list)
    
    end_of_game = False
    lives = 6
    while not end_of_game :
      guess = input("Guess your word: ").lower()
      for position in range(word_legth):
        letter = Choosen_word[position]
        if letter == guess :
          new_list[position] = letter
      print(new_list)
    
      if guess not in Choosen_word :
          lives -= 1
          if lives == 5 :
              print(stages[6])
          elif lives == 4 :
              print(stages[5])
          elif lives == 3 :
              print(stages[4])
          elif lives == 2 :
              print(stages[3])
          elif lives == 1 :
              print(stages[2])
          else :
              print(stages[2])
      print(lives)
    
      if "_" not in new_list and lives != 0 :
        end_of_game = True
        print("you_win")
      elif lives == 0 :
        print("you_lost")
        end_of_game = True

Day 8 Project - Caesar Cypher

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    end_of_game = False
    
    while not end_of_game :
    
        def encrypt(plain_text, shift_amount) :
            cipher_text = ""
            for letter in plain_text :
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            print(f"Encoded text is {cipher_text}")
            decryption =input("if you want to decrypt the word yes/no : ").lower()
            if decryption == "yes" :
    
                def decrypt(cipher_text, shift_amount):
                    New_cipher_text = ""
                    for letter in cipher_text :
                        position = alphabet.index(letter)
                        new_position = position - shift_amount
                        new_letter = alphabet[new_position]
                        New_cipher_text += new_letter
                    print(New_cipher_text)
    
                decrypt(cipher_text, shift_amount=shift)
    
        def decrypt(plain_text, shift_amount):
            New_cipher_text = ""
            for letter in plain_text:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                New_cipher_text += new_letter
            print(New_cipher_text)
    
        if direction == "encrypt" :
            encrypt(plain_text = text, shift_amount = shift)
            user_choice = input("whether you want to continue yes/ no : ")
            if user_choice == "yes":
                end_of_geme = False
            else :
                end_of_geme = True
        elif direction == "decrypt" :
            decrypt(plain_text = text, shift_amount=shift)

Day 9 Project - Bidding Game


    print("Welcome to bidding game")
    Bid_list = {}
    
    def find_highest_bidder(bidding_record):
        highest_bid = 0
        winner = ""
        for Bidder in bidding_record:
            bid_amount = bidding_record[Bidder]
            if bid_amount > highest_bid :
                highest_bid = bid_amount
                winner = Bidder
        print(f"Ther winner is {winner} with the bid amount $ {highest_bid}")
    
    
    Continue = False
    while not Continue :
        name = input("Enter bidder name : ")
        Price = int(input("Ask for bid price $: "))
        Bid_list[name] =  Price
        print(Bid_list)
    
        bidder = input("if any other bidder there yes/no : ")
        if bidder == "yes":
            Continue = False
        elif bidder == "no" :
            find_highest_bidder(bidding_record = Bid_list)

Day 10 Project - Calculator Project

    def Add(num1, num2):
        answer = num1 + num2
        print(answer)
        return answer
    
    def Sub(num1, num2):
        answer = num1 - num2
        print(answer)
        return answer
    
    def Mult(num1, num2):
        answer = num1 * num2
        print(answer)
        return answer
    
    def Divide(num1, num2):
        answer = num1 / num2
        print(answer)
        return answer
    
    operations =  {
        "+" : Add,
        "-" : Sub,
        "*" : Mult,
        "/" : Divide
    }
    
    num1 = float(input("Enter your 1st number : "))
    num2 = float(input("Enter your 2nd number : "))
    
    for symbols in operations:
        print(symbols)
    operation_symbol = input("Pick an operation from the line above : ")
    caculate_functions = operations[operation_symbol]
    answer = float(caculate_functions(num1, num2))
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    Continue = input("You want to continue the game play Y/N : ")
    num1 = answer
    num2 = float(input("Enter the new number 2 : "))
    
    if Continue == "Y":
        for symbols in operations:
            print(symbols)
        operation_symbol = input("Pick an operation from the line above : ")
        caculate_functions = operations[operation_symbol]
        answer = float(caculate_functions(num1, num2))
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    else :
        print("Thank you for using this")

Day 11 Project - Capstone Project

    import random
    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """
    
    def deal_card():
        """"Return randon card from the deck."""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card
    
    def Calculate_score(cards):
        """"Take a list of cards and return the score calculated from the cards"""
    
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21 :
            cards.remove(11)
            cards.append(1)
    
        return sum(cards)
    
    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw 🙃"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack 😱"
        elif user_score == 0:
            return "Win with a Blackjack 😎"
        elif user_score > 21:
            return "You went over. You lose 😭"
        elif computer_score > 21:
            return "Opponent went over. You win 😁"
        elif user_score > computer_score:
            return "You win 😃"
        else:
            return "You lose 😤"
    
    def play_game():
        print(logo)
        user_cards = []
        computer_cards = []
        Is_game_over = False
    
        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())
    
        user_score = Calculate_score(user_cards)
        computer_score = Calculate_score(computer_cards)
        print(f"your_cards: {user_cards} and current_scores: {user_score}")
        print(f"Computer's first card : {computer_cards[0]}")
    
        if user_score == 0 or computer_score == 0 or user_score > 21 :
            Is_game_over = True
        else:
            user_should_deal = input("Type 'Y' for take another card or Type 'N' to Pass : ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
            #Hinds 12
        while computer_score != 0 and computer_score < 17 :
          computer_cards.append(deal_card())
          computer_score = Calculate_score(computer_cards)
    
        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))
    
    
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
      play_game()

Day 12 Project - Number Guessing

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

Day 14 Project - Higher Vs Lower Game

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

Day 15 Project - Coffee Machine

    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }
    
    profit = 0
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    
    def is_resource_sufficient(order_ingredients):
        """Returned true when order can be made. False when ingredients are insufficient"""
        is_enough = True
        for item in order_ingredients:
            if order_ingredients[item] >= resources[item]:
                print(f"Sorry, There is no enough of {item}.")
                is_enough = False
        return is_enough
    
    def process_coins():
        """Returns the total calculated from the coins inserted."""
        print("please Insert Coins.")
        total = int(input("How many quarters? : ")) * 0.25
        total += int(input("How many dines? : ")) * 0.1
        total += int(input("How many nickles? : ")) * 0.05
        total += int(input("How many pennies? : ")) * 0.01
        return total
    
    def is_transaction_successful(money_received, drink_cost):
        """return True when payment accepted or False when the money is insufficient."""
        if money_received >= drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} dollars in change.")
            global profit
            profit += drink_cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
    
    def make_coffee(drink_name, order_ingredients):
        """Deduct the required ingredients from the resources"""
        for item in order_ingredients:
            resources[item] -= order_ingredients[item]
            print(f"Here is your {drink_name} ☕")
    
    
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resources["water"]}ml")
            print(f"Milk: {resources["milk"]}")
            print(f"Coffee: {resources["coffee"]}g")
            print(f"Money: ${profit}")
        else:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])

Day 16 Project - Python Turtle

    import turtle
    from turtle import Turtle, Screen
    
    timmy = Turtle()
    print(timmy)
    timmy.shape("turtle")
    timmy.color("coral")
    timmy.forward(100)
    
    my_screen = Screen()
    print(my_screen.canvheight)
    my_screen.exitonclick()

Day 17 Project - OOP with Coffee Machine Project

    from menu import Menu, MenuItem
    from coffee_maker import CoffeeMaker
    from money_machine import MoneyMachine
    
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()
    is_on = True
    
    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options})")
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker. is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

Day 19 Project - Turtle Race

    from turtle import Turtle, Screen
    import random
    
    
    screen = Screen()
    screen.setup(width = 500, height = 400)
    user_bet = screen.textinput(title = "Make your bed", prompt = "which turtle will win the race? Enter a color : ")
    colors = ("red", "orange", "yellow", "green", "blue", "purple")
    y_position = [-70, -40, -10, 20, 50, 80]
    all_turtles = []
    
    for turtle_index in range(0, 6):
        New_turtle = Turtle(shape = "turtle")
        New_turtle.color(colors[turtle_index])
        New_turtle.penup()
        New_turtle.goto(x=-230, y=y_position[turtle_index])
        all_turtles.append(New_turtle)
    
    is_race_on = True
    if user_bet :
        is_race_on = True
    
    while is_race_on:
    
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                print(turtle.color())
                winning_color = turtle.pencolor()
                if winning_color == user_bet :
                    print(f"you've won! the {winning_color} turtle is the winner!")
                    is_race_on = False
                else :
                    print(f"you've lost! the {winning_color} turtle is the winner!")
                    is_race_on = False
    
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
    
    
    
    
    
    
    
    
    
    screen.exitonclick()
