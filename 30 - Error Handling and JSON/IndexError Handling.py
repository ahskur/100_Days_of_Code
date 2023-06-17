import random

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + " pie")


make_pie(4)


# try:
#     make_pie(4)
# except:
#     make_pie(random.randint(1,3))
# finally:
#     print("Do you want Pie?")
