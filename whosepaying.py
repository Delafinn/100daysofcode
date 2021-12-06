import random

names_string = input("Give  everybody's first name, separated by a comma. ")
names = names_string.split(",")
print(names)
payer = random.choice(names)

print("the person paying the food bill is " + payer)
