Height = int(input("Enter your Height : "))
want_photoes = input("Do you want photoes yes/No : ")

if Height >= 120 :
    print("You can Ride")
    age = int(input("Enter your age : "))
    if age < 12 :
        print("You need to provide 5$ for Roller Coaster")
        your_price = 5
    elif age  >12 & age <18 :
        print("You need to provide 7$ for Roller Coaster")
        your_price = 7
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
