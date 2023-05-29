# Turtle module only work with .gifs
# That's why we're using a gif

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
# Let's use the image as a turtle shape so to speak
# We set a variable with the images path then use the screen func .addshape to make the shape usable
# and use turtle to call it
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

game_data = pandas.read_csv('50_states.csv')
states_list = game_data["state"].to_list()

# Add states already guessed here

guessed_states = []
while len(guessed_states) < 50:
    # Remember to put .title() at the end to avoid spelling cases like IdaHO or DelaWARE etc
    guess_state = screen.textinput(title=f"{len(guessed_states)} States correct", prompt="What's another state name?").title()
    # Debug print
    # print(guess_state)

    # Quit Game using a 'secret word'
    if guess_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                (missing_states.append(state))
        # Everytime the game exits, create a new .csv file with the States that weren't guessed so the user can learn
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    # You can only use 'in' if you convert first to a list
    if guess_state in states_list:
        guessed_states.append(guess_state)
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        location = game_data[game_data.state == guess_state]
        pen.goto(int(location.x), int(location.y))
        # Grabs the first element of the date - only it's value
        pen.write(guess_state)

# def get_mouse_click_coor(x,y):
#     # Def a function the can take inputs - x and y
#     # and print these values
#     print(x,y)
#
# # Everytime the screen is clicked, call the function to print the x and y values from where its clicked
# turtle.onscreenclick(get_mouse_click_coor)

# Keeps the window open/program running - Alternative to exitonclick()
# turtle.mainloop()
