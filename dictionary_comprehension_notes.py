# Dictionary Comprehension is a way to create a dictionary with shortened syntax

#new_dict = {new_key:new_value for item in list}also create a dictionary based on the values of an existing dictionary
#
# new_dict ={new_key:new_value for (key,value) in dict.items() if test }


names = ["bob", "frank", "bobby", "benjamin", "Robert" , "julian", "mario", "dave"]


import random

student_scores = {student:random.randint(1,101) for student in names }

print(student_scores)


# create a dictionary called past students

passed_students = {student:score for (student, score) in student_scores.items() if score > 60}

print(passed_students)

# creating a dictionary from a string in python
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}


print(result)


# creating a dictionary from a dictionary and maniplulating the data to the new dictionary
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}

print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(key)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

answer = input("type any word").upper()

phonetic_word = [phonetic_dictionary[letter] for letter in answer]

print(phonetic_word)
