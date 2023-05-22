# ### Understanding Scope ###
# # Global scope - Defined at top level (not inside a function) and available to all the code to use
# enemies = 1
# # Local Scope
# def increase_enemies():
#       enemies = 2
#       print(f"enemies inside function: {enemies}")
# # Because the variable 'enemies' is INSIDE the function, it's only accessible INSIDE the function, = Local Scope
# increase_enemies()
# print(f"enemies outside function:{enemies}")
#
# # Functions can also be 'nested' in another functions as to be local scope only
# def game():
#       """You can only call spawn_enemies when you're INSIDE the function game - else you'll have errors"""
#       def spawn_enemies():
#             potion_amount = 2
#             print(potion_amount)
#
# # There is no Block Scope in Python
# # You can use variables that are in if/else/ statements but cannot use variables that are within FUNCTIONS
# # aka Functions are 'scopped', but normal indentations not!

####### Modifying Global Scopes #######

# # Create a Global Scope Variable
# enemies = 'Skeleton'
# # Create function that tries to modify the variable
# def increse_enemies():
#       enemies = 'Zombie'
#       print(f"Enemies INSIDE this function: {enemies}")
# # Call the function
# increse_enemies()
# print(f"Enemies OUTSIDE - as Global Scopes: {enemies}")

# # Create a Global Scope Variable
# enemies = 1
# # Create function that tries to modify the variable
# def increse_enemies():
#       """This 'global' takes the variable OUTSIDE of the scope and brings it in.
#       This induces hard to debug problems because you're bringing a global variable to something that is locally scopped"""
#       global enemies
#       enemies += 1
#       print(f"Enemies INSIDE this function: {enemies}")
#
# # Call the function
# increase_enemies()
# print(f"Enemies OUTSIDE - as Global Scopes: {enemies}")

# # Create a Global Scope Variable
# enemies = 1
#
# # Create function that tries to modify the variable
# def increase_enemies():
#     """But you can also just use RETURN to update the variable for exemple without using global"""
#     print(f"Enemies INSIDE this function: {enemies}")
#     return enemies + 1
#
# # Call the function
# enemies = increase_enemies()
# print(f"Enemies OUTSIDE - as Global Scopes: {enemies}")

###### Global Constants ########

# Make them UPPERCASE so you remember to NOT MODIFY THEM
PI = 3.14159
URL = "www.google.com"
TWITTER_HANDLE = '@queijoquente'
