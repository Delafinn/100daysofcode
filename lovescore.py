
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lowercase_combinednames = combined_names.lower()

t = lowercase_combinednames.count("t")
r = lowercase_combinednames.count("r")
u = lowercase_combinednames.count("u")
e = lowercase_combinednames.count("e")
true = t + r + u + e

l = lowercase_combinednames.count("l")
o = lowercase_combinednames.count("o")
v = lowercase_combinednames.count("v")
e = lowercase_combinednames.count("e")

love = l + o + v + e

lovescore = str(true) + str(love)
print(lovescore)

if int(lovescore) < 10:
  print("your lovescore is low")
elif int(lovescore) <= 40:
  print("your lovescore is so so")
else:
  print("your lovescore is high")
