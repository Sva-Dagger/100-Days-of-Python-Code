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
