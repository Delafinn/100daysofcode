#Password Generator Project
import random
import sys

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
capletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '$', '%', '&','*', '+']

full_list = letters + numbers + symbols + capletters

#lists above contain characters used in passwords


print("Welcome to quick password generator")
RUN_PROGRAM = True

while RUN_PROGRAM is True:
    proceed_question = input("would you like to proceed?").lower()
    if proceed_question == "no" or proceed_question == "n":
        sys.exit()

    elif proceed_question == "yes" or proceed_question == "y":
        n_characters = int(input("How many characters would you like in your password? Please enter a number."))
        passwordlist = []  #starting with en empty list
        for i in range(0, n_characters):
            passwordlist.append(random.choice(full_list)) #adding to the empty passwordlist randomly from full_list
        random.shuffle(passwordlist) #shuffling the passwordlist
        password = "" #now we make an empty string
        # we are making a string so the generated password is readable to the human eyes. and not in a list separated by commas.

        for items in passwordlist: # from i or items in passwordlist
            password += items # add i or items to the string password

        print(password) #print password
