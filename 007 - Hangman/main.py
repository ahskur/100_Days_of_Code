import random
import hangman_words
import hangman_art

#Selecting a random word to start the game
from hangman_words import word_list
chosen_word = random.choice(word_list)
#Ask user to guess a letter and make it lowercase

#Debug
print(f"The answer is {chosen_word}.")
# Lets also create the amount of lives a player has

lives = 6
# Lets import the logo from the art file
from hangman_art import logo
print(logo)


#Create blanks that is a list where the selected word in going to be printed as _
display = []
for letter in chosen_word:
    display += "_"

#Now let's do a while loop for the player to input as many letters as he can until he's got the word
end_of_game = False
while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    #lets also check if they've already tried the letter they're inputing
    if guess in display:
        print(f"You've already guessed {guess}.")

    #Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word - You lose a life! =(")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose! :(")
    print(display)

    #Check if user has got all letters yet
    if "_" not in display:
        end_of_game = True
        print("You win!")
    # This prints the stages of the hangman in accord of how many lives are still left
    from hangman_art import stages
    print(stages[lives])