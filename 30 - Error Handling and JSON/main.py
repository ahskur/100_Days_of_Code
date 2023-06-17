# # FileNotFound
# # with open("a_file.txt") as file:
# #   file.read()
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["non_existent_key"])
# except FileNotFoundError:
#     #print("There is no file with that name.")
#     # Using the write method, the file is going to be created if it doesn't already exist
#     open("a_file.txt","w")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This error was made up! =)")
#     # file.close()
#     # print("The program ended and files were close.")

height = float(input("Height:"))
weight = int(input("Weight: "))

bmi = weight / height ** 2
print(bmi )







# KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple","Banana","Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)
