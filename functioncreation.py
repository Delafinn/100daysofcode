'''This code is not meant to be ran and is only meant for educational purposes and
explaination of functions in  python '''


# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
  print("Hello there!")
  print("how do you do?")
  print("its a nice toay. ")

greet()


def greet_with_name(name):
  print(f"hello there! {name} ")
  print(f"how do you do? {name} ")
  print(f"its a nice today. {name} wouldn't you agreee?")


greet_with_name("finn")


# functions with more than one input

def greet_with_name_and_location(name, location):

  print(f"hello there! {name} ")
  print(f"how do you do? {name} ")
  print(f"its a nice today. {name} wouldn't you agreee?")
  print(f"whats it like in {location} ? ")

greet_with_name_and_location("finn", "salt lake city")

# using keyword arguements in functions rather than locaton arguements
def greet_with_name_and_location(name, location):

  print(f"hello there! {name} ")
  print(f"how do you do? {name} ")
  print(f"its a nice today. {name} wouldn't you agreee?")
  print(f"whats it like in {location} ? ")

greet_with_name_and_location( location = "salt lake city",name = "finn")

### how many paint cans do we need function
# for class use only.

import math
def paint_calc(height, width, cover):
  area = test_h * test_w
  numberofcans = math.ceil(area / cover)
  cans = numberofcans
  print("the number of cans you need is:" + str(cans))


test_h = int(input("Height of wall in meters: "))
test_w = int(input("Width of wall in meters: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
