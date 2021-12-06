import random


while True:
    flip = ["heads", "tails"]
    coin_flip = input("want to flip a coin?").lower()
    if coin_flip == "yes":
        choice = random.choice(flip)
        print("the coin flip came up as:" + str(choice))
    if coin_flip == "no":
        quit()
