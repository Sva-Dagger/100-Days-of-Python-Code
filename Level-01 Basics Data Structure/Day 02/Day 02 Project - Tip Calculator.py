Total_bill = float(input("Enter your total bill in $ "))

Tip_in_percent = (float(input("Enter your Tip in % "))/100)

Tip = (Total_bill*Tip_in_percent)

bill_with_Tip = Total_bill + Tip

Sharing_persons = int(input("Enter total number of sharing persons "))

Total_Shared_Bill = (round(bill_with_Tip/Sharing_persons, 2))

print(f"Each Person Should Pay {Total_Shared_Bill}$")
