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