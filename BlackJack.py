############### Blackjack Project #####################
import random
import sys
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

  # define a end_game function for the end of the game
def end_game():
    if sum_of_userscards > 21:
        print("you bust! dealer wins!.")

    elif sum_of_userscards == 21:
        print("winner winner chicken dinner! 21!! \n you win!")

    elif sum_of_userscards > sum_of_dealerscards and sum_of_userscards < 21:
        print("you win!")

    elif sum_of_dealerscards > 21:
        print("you win!")

    elif sum_of_dealerscards > sum_of_userscards and sum_of_dealerscards < 21:
        print("dealer wins!")

    elif sum_of_dealerscards == 21:
        print("dealer wins!")

    elif sum_of_userscards == 21 and sum_of_dealerscards == 21:
        print("you win!")

# definiing the mechanics of blackjack

deck = [11 , 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # values of cards
users_cards= [] # empty list of users cards
dealers_cards = [] # empty list of users cards


# dealing cards to user and dealer
users_card1 = random.choice(deck) # users first card
users_cards.append(users_card1) # add the first card to the users empty list

users_card2 = random.choice(deck) # users second card
users_cards.append(users_card2) # add the second card to the empty list

print(f" Your cards are {users_cards}")  # showing the user their card values
sum_of_userscards = sum(users_cards) # add the users card values to get the sum
print(f"total amount of your cards: {sum_of_userscards} ") # print the total amount of the users cards


dealers_card1 = random.choice(deck) # dealers first card
dealers_cards.append(dealers_card1) # add the first card to the dealers empty list

dealers_card2 = random.choice(deck) # dealers second card
dealers_cards.append(dealers_card2) # add the second card to the dealers empty list

print(f" the dealers cards are {dealers_cards}")  # showing the user the dealers card value
sum_of_dealerscards = sum(dealers_cards)  # add the dealers card values to get the sum
print(f"total amount of dealer cards: {sum_of_dealerscards} ") # print the total amount of the dealers cards

if sum_of_userscards == 21:
    end_game()


# we should use a while loop for hit or pass

while True: # a while loop for the users portion to hit or stand
    hit_or_stand = input("would you like to hit or stand?").lower() # asking the user if they want to hit or stand
    if hit_or_stand == "quit":  # this is a quit option mainly used for debugging but can be used in game.
        sys.exit()
    elif hit_or_stand == "hit": #
        users_card3 = random.choice(deck)
        print(f"the card was {users_card3}")
        users_cards.append(users_card3)
        sum_of_userscards = sum(users_cards)
        if users_card3 == 11 and sum_of_userscards > 21:
            users_card3 = 1
            print(f"the new total amount of your cards is: {sum_of_userscards} ")
            if sum_of_userscards == 21:
                end_game()

        elif sum_of_userscards > 21:
            end_game()

        else:
            print(f"the new total amount of your cards is: {sum_of_userscards} ")
            continue
    elif hit_or_stand == "stand":
        break

print("dealers turn!")
while True:
    if sum_of_dealerscards < sum_of_userscards and sum_of_dealerscards < 21:
        dealers_card3 = random.choice(deck)
        print(f"the dealer pulled a new card  it was a {dealers_card3}")
        dealers_cards.append(dealers_card3)
        sum_of_dealerscards = sum(dealers_cards)
        if dealers_card3 == 11 and sum_of_userscards > 21:
            dealers_card3 = 1
            if sum_of_dealerscards == 21:
                end_game()
        print(f"the dealers card amount is: {sum_of_dealerscards}")
        if sum_of_dealerscards > sum_of_userscards or sum_of_dealerscards > 21:
            end_game()
            break
        elif sum_of_dealerscards < sum_of_userscards:
            continue
    elif sum_of_dealerscards > sum_of_userscards:
        end_game()
        break
