print("tip calculator!")
total = float(input("what was the total bill?"))
tip_percent = input("How much tip would you like to give? 15 or 20 percent?")
how_many_people = input("How many people to split the bill?")

percentage = float(tip_percent) / 100  # making the tip percentage

tipamount = int(total) * float(percentage) # get the tip amount

print("the tip amount is" + str(tipamount)) # showing the tip amount

# bill amount + tip
bill = int(total) + int(tipamount)
print("the total bill with Tip is")
print(bill)

# divided by users
endtotal = int(bill) / int(how_many_people)
print("Everyone is going to have to pay")
print(round(endtotal, 2))
