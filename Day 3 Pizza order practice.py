print("Thank you for choosing Python Pizza Deliveries!")
bill = 0
final_bill = 0
size = input("Enter your pizza Size S/M/L : ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N : ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N") # Do you want extra cheese? Y or N
if (size == "S"):
  bill_1 = bill + 15
elif(size == "M"):
  bill_1 = bill + 20
elif(size == "L"):
  bill_1 = bill + 25
else:
  bill_1 = bill + 0
if(add_pepperoni == "Y"):
  if (size == "S"):
    bill_2 = bill_1 + 2
  elif (size == "M" or size == "L"):
    bill_2 = bill_1 + 3
  else:
    bill_2 = bill_1 + 0
  bill_3 = bill_2
else:
  bill_3 = bill_1 + 0
if (extra_cheese == "Y"):
  final_bill = bill_3 + 1
else:
  final_bill = bill_3 + 0
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
print(f"Your final bill is: ${final_bill}.")