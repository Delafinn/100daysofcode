import random
wordlist = ["this", "is", "word", "love", "cowboy", "hardware", "reason", "raspberry", "pwned", "bees", "cheese", "fees", "winter",
"fall", "spring", "summer", "water" , "land", "googel", "found", "pound" , "dog" , "mob", "cat", "job" , "car", "bar" "star"]  # my smallwordlist
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']  #provided diagrams


chosenword = random.choice(wordlist) # randomly selecting a word from the wordlist
word_length = len(chosenword) # making a variable equal  to the length of the chosenword in a number
display = []  # making an empty display

for letter in range(0, word_length): # for each letter in a range from 0 to the value of word_length
    display += "_" # add an a blank

print(display) # printing the blanks of each letter
#print(chosenword)
lives = 6 # 6 lives for 6 body parts
print("welcome to hangman!") # welcome the user

endgame = False # end game while loop
while endgame == False:

    guess = input("what letter do you want to guess?").lower() # asking user to choose a letter

    for position in range(word_length): # for each character position in the chosenword
        letter = chosenword[position]  # assign that position the variable letter
        if letter == guess: # if the variable letter is equal to your guess
            display[position] = letter # replace the letter with the positon on the display

    print(display) # display the positon of the letter. within the chosenword
    if guess in chosenword:
        print("you guessed a word correctly.") # letting the user know they guessed correctly

    if guess not in chosenword: # if user is wrong
        lives -= 1 # take away a life
        if lives == 0: #checking to see if the users lifes are at 0
            end_of_game = True # trigger end_of_game
            print("You lose.") #  end_of_game
        else:
            print("you are wrong!") # leting the user know they were wrong
    if "_" not in display: # winning dialog
        endgame = True # another end_of_game trigger
        print("you win!")  #  end_of_game
    print(stages[lives]) # always print the provided diagrams
