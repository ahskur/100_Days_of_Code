from Auction_logo import logo
print(logo,"\nWelcome to the Blind Auction Assistant - Let's get some bids in!")
bid_dict = {}
end_of_bid = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}!")

while not end_of_bid:
    who = input("Who will be bidding now?:\n")
    bid = int(input("How much do you want to bid?: \n$"))
    bid_dict[who] = bid
    next_bidder = input("Are there other bidders? 'Y' for yes, 'N' for no.").lower()
    if next_bidder == "n":
        end_of_bid = True
        find_highest_bidder(bid_dict)
