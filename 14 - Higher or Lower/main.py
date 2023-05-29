# display logo
# pull a random account from game data
# format account data to printable format
# ask for guess
# compare answer/check if guess is correct
# give feedback on guess
# update score
# make game repeatable
# make account at B to A if guessed right

from art import logo,vs
from game_data import data
import random

print(logo,"\nWelcome to Higher or Lower!\nWould you like to begin?! - Type 'y' for yes, 'n' for no and 'help' for information!")
choice = input("> ").lower()
### SET GAME SCORE
score = 0
### SET BOOLEAN FLAG TO END GAME
game_end = False

#### FUNCTION TO FORMAT DATA FROM THE LIST #######
def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_description}, from {account_country}")
#### FUNCTION TO COMPARE THE ANSWER GIVEN #######
def compare_answer(answer,follower_count_A,follower_count_B):
    """Take user answer and compare follower count to see if the user got it right"""
    if follower_count_A > follower_count_B:
    # Only return if answer == a aka return True
        return answer == "a"
    else:
        return answer == "b"
### This is to make so that when guesses right, B becomes A and B becomes a new account to compare
B = random.choice(data)

while not game_end:
    if choice == 'y':
        print("Alright, let's start the game!")
        ### This is to make so that when guesses right, B becomes A and B becomes a new account to compare
        A = B
        B = random.choice(data)
        while A == B:
            B = random.choice(data)

        follower_count_A = A["follower_count"]
        follower_count_B = B["follower_count"]

        print(f"Compare A: {format_data(A)}")
        print(vs)
        print(f"Against B: {format_data(B)}")

        answer = input("Who has more followers? Type 'A' or 'B'\n").lower()

        is_correct = compare_answer(answer, follower_count_A, follower_count_B)
        if is_correct:
            score += 1
            print("You're right!")
        else:
            print(f"Sorry, that's wrong! Your final score is {score}.")
            game_end = True

    elif choice == 'n':
        print("Okey dokey - Have a nice day!")
        game_end = True

    elif choice == 'help':
            print("You'll be shown two names of celebrities - You need to chose which one has the bigger amount of followers on Instagram. "
                  "If you are correct, you win a point and go to the next round!\nIf you didn't got it right - No worries, you can always play again!")


