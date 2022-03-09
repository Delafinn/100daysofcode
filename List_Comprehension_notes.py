numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆



# using a for loop to add the squared_numbers to a new list
squared_numbers = []
for number in numbers:
  answer = number * number
  squared_numbers.append(answer)

# key/template for list comprehensions
#
# example = [new_item for item in list if test]

# using a list comprehension to do the same as the for loop

squared_numbers = [ n * n for n in numbers]

# other examples of adding each letter in the name string
name = "finn"

letter_list = [letter for letter in name ]

# list comprehension within a range
therange = range(1,5)

range_list = [number * 10 for number in therange]

# list comprehension within lists &list comprehension with tests/ if statements
names = ["bob", "frank", "bobby", "benjamin", "Robert" , "julian", "mario", "dave"]

short_names = [name for name in names if len(name) < 6]

cap_names = [name.upper() for name in names if len(name) > 5]

# list comprehension with even numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [number for number in numbers if number % 2 == 0]


# opening a example file and using it in a list comprehension
# with open("file1.txt") as num_list1:
#   list1 = num_list1.readlines()
#
# with open("file2.txt") as num_list2:
#   list2 = num_list2.readlines()
#
#
# result = [int(n) for n in list1 and list2 if n == n]
#
#
# print(result)






print(squared_numbers)
print(letter_list)
print(range_list)
print(short_names)
print(cap_names)
print(result)
