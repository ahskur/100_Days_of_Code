import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_amount = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_amount = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_amount = len(data[data["Primary Fur Color"] == "Black"])


print(grey_squirrel_amount)
print(red_squirrel_amount)
print(black_squirrel_amount)

data_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[grey_squirrel_amount,red_squirrel_amount,black_squirrel_amount]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count.csv")