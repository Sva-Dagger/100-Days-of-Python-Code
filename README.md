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
