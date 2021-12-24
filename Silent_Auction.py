from replit import clear # used to clear previous users entry


bids = {} # an empty dictionary of bids
end_bid = False # while loop state


def find_highest_bidder(bidding_record): # function to find the highest bidder
  highest_bid = 0 # highest bid is starting at 0
  for bidder in bidding_record: # for each bidder in the bidding record
    bid_amount = bidding_record[bidder] # the bid amount references the bidder and their bid amount from the bids dictionary
    if bid_amount > str(highest_bid):  # if the bidders amount is higher than the current highest bid
      highest_bid = bid_amount # then the users bid amount is now the highest bid the for loop with loop through each bidder
      winner = bidder # winner is the bidder with the highest bid_amount
  print(f"the winner is {winner} they won with amount of ${bid_amount}") # printing the winner to console

 # main program
while end_bid == False: # while end_bid isn't True
    print("Welcome to the Silent Auction! ")
    name = input("what is your name?")  # getting the bidders name
    price = input(str("what is your bid amount? $")) # getting the bidders dollar amount
    bids[name] = price # bids refers back to the empty dictionary on line 4 adding the name as the key and the price or bid amount as the value of the key
    more_users = input("Is another user bidding?") # Console asking if their are more users
    clear()
    if more_users == "no" or more_users == "n": # ending the bidding
        end_bid = True # trigger set to end main program
        find_highest_bidder(bids) # final output
