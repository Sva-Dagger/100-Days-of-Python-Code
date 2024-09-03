Height = int(input("Enter your Height : "))

if Height >= 120 :
    print("You can Ride")
    age = int(input("Enter your age : "))
    if age < 12 :
        print("You need to provide 5$")
    elif age  >12 & age <18 :
        print("You need to provide 7$")
    else :
        print("You need to provide 12$")
else:
    print("You can't Ride")
