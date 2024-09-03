Height = int(input("Enter your Height : "))
age = int(input("Enter your age : "))

if Height >= 120 :
    print("You can Ride")
    if age >= 18 :
        print("You need to provide 12$")
    else :
        print("You need to provide 7$")
else:
    print("You can't Ride")
