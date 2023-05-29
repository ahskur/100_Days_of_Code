# data = []
# data_file = open('weather_data.csv','r')
# data = data_file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')
# print(data)
# print(data["temp"])
#
# data_dictionary = data.to_dict()
# print(data_dictionary)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # average_temp = sum(temp_list) /len(temp_list)
# # print(average_temp)
#
# average_temp = data["temp"].mean()
# print(average_temp)
#
# max_temp = data["temp"].max()
# print(max_temp)

# Get Data in a Row
print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
temp_monday = int(monday.temp)
temp_monday_F = temp_monday * 9/5 + 32
print(temp_monday_F)

# Create Dataframe (Spreadsheet) from scratch
data_dict = {
    "students":["Amy", "James", "Angelina"],
    "scores":[76,67,54]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")