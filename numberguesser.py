#Number Guessing Game

# Allow the player to submit a guess for a number between 1 and 100.
import random
import time

guesses = int(0)

random_number = random.randint(1,101)


print("Welcome to the number guessing game!")
difficulty = input("what difficulty do you want? easy mode or hard mode?")
if difficulty == "easy" or difficulty == "e":
    guesses += 6
elif difficulty == "hard" or difficulty == "h":
    guesses  += 2
print(f"you have {guesses} during this match!")
while guessed_number != random_number:

    guessed_number = input("I am thinking of a number. it is between one and one hundred. \n Guess the number!")
    guessed_number = int(guessed_number)

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.

    if guessed_number == random_number:
        print("you have luckily guessed the right number! you win!")
        print(f"the random number was: {random_number}")
        time.sleep(2)


    elif guessed_number > random_number:
        print("oof, the number you guessed was too high, guess again.")
        time.sleep(2)
        guesses -= 1
        continue

    elif guessed_number < random_number:
        print("oof, the number you guessed was too low, guess again.")
        time.sleep(2)
        guesses -= 1
        continue

if guesses == 0:
    print(f"Oh no! you lose! \n the random number was : {random_number}")

# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
