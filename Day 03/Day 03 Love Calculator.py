print("The Love Calculator is calculating your score...")
name1 = input("Enter your Name") # What is your name?
name2 = input("Enter your loved ones name") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name = name1 + name2
lower_name = combined_name.lower()

T = lower_name.count("t")
R = lower_name.count("r")
U = lower_name.count("u")
E = lower_name.count("e")
Word_1 = T + R + U + E

L = lower_name.count("l")
O = lower_name.count("o")
V = lower_name.count("v")
E = lower_name.count("e")
Word_2 = L + O + V + E

Your_result = str(Word_1) + str(Word_2)
Your_result = int(Your_result)
if((Your_result < 10) or (Your_result > 90)):
  print(f"Your score is {Your_result}, you go together like coke and mentos.")
elif((Your_result >= 40) and (Your_result <= 50)):
  print(f"Your score is {Your_result}, you are alright together.")
else:
  print(f"Your score is {Your_result}.")
