from logo import auction_bid
print(auction_bid)
bid_dictionary={}
person_cheak=input("Is there any Bidder 'yes', 'no' : ").lower()

while person_cheak=='yes':
    bidder_name=input(" Whats your name : ").upper()
    bid_price=int (input("Tell your Bid price : "))
    bid_dictionary[bidder_name]=bid_price
    person_cheak=input("Is there any other Bidder : ").lower()
    print("\n"*100)
max=0

for bid in bid_dictionary:
    if max<bid_dictionary[bid]:
        max=bid_dictionary[bid]
for win in bid_dictionary:
    if bid_dictionary[win]==max:
        print(f"Winner of this Auction is   {win} with highest price made : {bid_dictionary[win]}")
    
