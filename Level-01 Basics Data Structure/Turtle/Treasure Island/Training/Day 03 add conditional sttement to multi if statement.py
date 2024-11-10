Height = int(input("Enter your Height : "))

if Height >= 120 :
    print("You can Ride")
    want_photoes = input("Do you want photoes yes/No : ")
    age = int(input("Enter your age : "))
    if age < 12 :
        print("You need to provide 5$ for Roller Coaster")
        your_price = 5
    elif age <= 18 :
        print("You need to provide 7$ for Roller Coaster")
        your_price = 7
    elif age >= 45 and age <= 56 :
        print("Everything is going to be ok. Have a free ride on us")
        your_price = 0
    else :
        print("You need to provide 12$ for Roller Coaster")
        your_price = 12

    if want_photoes == "yes":
        Total_Price = your_price + 3
        print(f"Your Total price {Total_Price}$ with Photoes")
    else :
        print(f"Your Total price {your_price}$ without Photoes")
else:
    print("You can't Ride")
