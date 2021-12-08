#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
capletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '$', '%', '&','*', '+']

fulllist = letters + numbers + symbols +capletters

#lists above contain characters used in passwords


print("Welcome to quick password generator")

n_characters = int(input("How many characters would you like in your password?"))


passwordlist = []  #starting with en empty list

for i in range(0, n_characters): # telling the computer how many characters we are gonna loop for
  passwordlist.append(random.choice(fulllist)) #adding to the empty passwordlist randomly from fulllist

random.shuffle(passwordlist) #shuffling the passwordlist

password = "" #now we make an empty string

for items in passwordlist: # from i or items in passwordlist
  password += items # add i or items to the string password

print(password) #print password
