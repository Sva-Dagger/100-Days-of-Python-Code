import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

users_Choice = int(input("Enter your choice bu Type 0 for Paper 1 for rock and 2 for Scissor"))
print(users_Choice)
Computer_Choice = random.randint(0, 2)
print(Computer_Choice)
if Computer_Choice == 0 and users_Choice == 1:
  print(f"users Choice is {rock}")
  print(f"Computer Choice is {paper}")
  print("You_Win")
elif Computer_Choice == 1 and users_Choice == 0 :
  print(f"users Choice is {paper}")
  print(f"Computer Chose {rock}")
  print("You_Win")
elif Computer_Choice == 2 and users_Choice == 1:
  print(f"Computer Chose {scissors}")
  print(f"users Choice is {paper}")
  print("You_Win")
elif Computer_Choice == 1 and users_Choice == 2:
  print(f"Computer Chose {scissors}")
  print(f"users Choice is {paper}")
  print("You_Win")
else :
  print("You_lost")