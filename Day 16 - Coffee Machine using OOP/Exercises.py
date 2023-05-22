# from turtle import Turtle, Screen
# turtle_is_go = True
# # Using turtle. we are tapping into the the module and pulling the Turtle() class
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red","blue")
# timmy.fd(30)
# while turtle_is_go:
#     timmy.fd(7)
#     timmy.right(6)
#     timmy.left(1)
#     timmy.hideturtle()
#
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokémon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"

print(table)

