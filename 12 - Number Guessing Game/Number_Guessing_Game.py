# TODO
# Ask if the player wants to go again and reset flag/game
# Make so the game recognizes if the inputted guess is not an integer and ask for a new number input

from art import what, wot_mate, logo, death, victory
import random
print(logo)
print("Welcome to the Number Guessing Game!\nI'm going to think of a number between 1 and 100 - Can you guess it correctly before meeting the sweet kiss of Death?")

# Define a global variable for the amount of lives
# This can also be local scoped - I don't know why I'm doing it this way tbh
number_lives = 0

# Define a variable to save the number the computer chose
number = 0
# Define a variable to save the user's guess
guess = 0

# Define boolean to end game
game_end = False

# Define a function to think of a random number
def think_of_number():
    chosen_number = random.choice(range(1, 100))
    print(f"I've thought of a number, can you guess it? You have {number_lives} attempts!")
    ## Debug print
    #print(chosen_number)
    return number + chosen_number

# Define a function to take a life away when guessed wrong
def lose_live():
    return number_lives - 1
    print(f"You lost a live, you now have {number_lives} attempts!")

while not game_end:
    chosen_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

######## EASY MODE ############
    if chosen_difficulty == 'easy':
        # Set the number of lives for the chosen mode - this is changing the value of the global variable!
        number_lives = 10
        # Call the function and set number to be guessed
        number = think_of_number()
        # Start of main loop of the game
        while guess != number and not game_end:
            # If the player didn't find the number or if he still has more lives than 0, he can input another number
            if number_lives == 0:
                print("You've lost! Bye bye now!")
                print(death)
                game_end = True
            else:
                guess = int(input("Guess a number: "))
            # Now check how high or low the number is
            # This if statement only goes through IF the above ones also didn't go through, else the game ends
                if guess == number:
                    print(victory,"YES, YOU DID IT - You won't die today!")
                    game_end = True
                elif guess < number:
                    number_lives = lose_live()
                    print(f"Too low! You have {number_lives} attempts left!")
            # Also accounting for extreme cases where numbers bigger than 100 are inputted
                elif guess > number and guess <= 100:
                    number_lives = lose_live()
                    print(f"Too high! You have {number_lives} attempts left!")
                elif guess > 100:
                    print("I'm sure I said from 1 to 100!\n",wot_mate)
                    number_lives = lose_live()

######## HARD MODE ###########
    elif chosen_difficulty == 'hard':
        # Set the number of lives for the chosen mode
        number_lives = 5
        # Call the function and set the number to be guessed
        number = think_of_number()
        # Start of the main loop - If the guessed number still isn't the chosen random number AND the flag hasn't
        # been triggered yet
        while guess != number and not game_end:
        # If the player didn't find the number or if he still has more lives than = 0, he can input another number
            if number_lives == 0:
                print("You've lost! Bye bye now!")
                print(death)
                game_end = True
            else:
                guess = int(input("Guess a number: "))
        # Now check how high or low the inputted number is
        # This if statement only goes through IF the above ones also didn't go through, else the game ends
                if guess == number:
                    print(victory,"YES, YOU DID IT - You won't die today!")
                    game_end = True
                elif guess < number:
                    number_lives = lose_live()
                    print(f"Too low! You have {number_lives} attempts left!")
            # Also accounting for extreme cases where numbers bigger than 100 are inputted
                elif guess > number and guess <= 100:
                    number_lives = lose_live()
                    print(f"Too high! You have {number_lives} attempts!")
                elif guess > 100:
                    print("I'm sure I said from 1 to 100!\n",wot_mate)
                    number_lives = lose_live()

# If the user tipped something other than 'easy' or 'hard'
    else:
        print("I didn't understand that, sorry! =(")
        print(what)

# go_again = input("Do you want to play again? Type 'y' for yes, 'n' for no.\n")
# if go_again == 'y':
#     game_end = False
# else:
#     print("Thanks for playing the Number Guessing Game!")
