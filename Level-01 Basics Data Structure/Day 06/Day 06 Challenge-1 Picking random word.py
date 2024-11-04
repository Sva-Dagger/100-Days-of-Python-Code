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
