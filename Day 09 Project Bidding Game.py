
print("Welcome to bidding game")
Bid_list = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for Bidder in bidding_record:
        bid_amount = bidding_record[Bidder]
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = Bidder
    print(f"Ther winner is {winner} with the bid amount $ {highest_bid}")


Continue = False
while not Continue :
    name = input("Enter bidder name : ")
    Price = int(input("Ask for bid price $: "))
    Bid_list[name] =  Price
    print(Bid_list)

    bidder = input("if any other bidder there yes/no : ")
    if bidder == "yes":
        Continue = False
    elif bidder == "no" :
        find_highest_bidder(bidding_record = Bid_list)
