import random

####################################################
# List Comprehension
####################################################
numbers = [1,1,2,3,5,8,13,21,34,55]

# # Exercise 1
# squared_numbers = [n*n for n in numbers]
# print(squared_numbers)

# # Exercise 2
# result = [n for n in numbers if n%2 == 0]
# print(result)

# # Exercise 3
# f1 = open("file1.txt","r")
# # Create a list with integers from file 1
# f1_numbers = [int(n) for n in f1]
# # Create a list with integers from file 2
# f2 = open("file2.txt","r")
# f2_numbers = [int(n) for n in f2]

# # Debug print
# print(f1_numbers,"\n",
#       f2_numbers)
#
# common_numbers = [num for num in f1_numbers if num in f2_numbers]
#
# print(common_numbers)

####################################################
# Dictionary Comprehension
####################################################
names = ["Alex", "Beth","Caroline", "Dave", "Hermann","Eleanor","Freddie","Mercury"]
#
# ### student_scores = {new_key:new_value for item in list}
#
# # Create random scores for each key inside the dictionary
# student_scores = {student:random.randint(20,100) for student in names}
# print(student_scores)
#
# # Using condition to put students who passed (note > 65) inside a new dictionary
# # new_dict = {new_key:new_value for (key,value) in dict.items()}
# passed_students = {student:score for (student, score) in student_scores.items() if score > 65}
# print(passed_students)

# # Exercise 1
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words_list = sentence.split()
# result = {word:len(word) for word in words_list}
# print(result)

# # Exercise 2
# Transform temperatures inside dictionary to fahrenheit
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {day:(temp_c * 9/5) + 32 for (day,temp_c) in weather_c.items()}
# print(weather_f)

# # Exercise 3 - Iterate over DataFrame from Pandas
# import pandas
#
# student_dict = {
#       "student":["Angela","James","Lily"],
#       "score":[56,76,98]
# }
# student_dataframe = pandas.DataFrame(student_dict)
# print(student_dataframe)
#
# # Loop trough row of the data frame
# for (index,row) in student_dataframe.iterrows():
#       # print(row.student, row.score)
#       if row.student == "James":
#             print(row.score)
