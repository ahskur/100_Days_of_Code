# Black Jack or 21 - Goal of the game is add card numbers but stay lower than 21
# If you go over 21 it's a Bust and you lose immediately
# 'As' can be worth 1 or 11

# Let's make it easier:
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
from art import logo
import random
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_scores(cards):
    """Take a list of cards and calculates the sum of them"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(dealer_score,user_score):
    """Compare scores between dealer and player"""
    if user_score > 21 and dealer_score > 21:
        return "You went over 21, you lose!"
    if user_score == dealer_score:
        return "Draw!"
    elif dealer_score == 0:
        return "Lose, Computer has 21!"
    elif user_score == 0:
        return "You've 21, you win!"
    elif user_score > 21:
        return "You went over 21, you lose!"
    elif dealer_score > 21:
        return "Computer went over 21, you win!"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():

    print(logo)
    # Two startings lists with nothing inside
    dealer_hand = []
    player_hand = []

    # Stating a boolean so the game can end when triggered
    is_game_over = False

    # Needs to loop twice to give out 2 cards - One each time
    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append((deal_card()))
    # Making a while loop so the game keeps going until the flag is reversed or triggered
    while not is_game_over:
        # Calculate the user score to see who's winning or even if the game is over
        user_score = calculate_scores(player_hand)
        dealer_score = calculate_scores(dealer_hand)
        print(f"Your cards: {player_hand}, current score: {user_score}.")
        print(f"Computer's first card: {dealer_hand[0]}.")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == 'y':
                player_hand.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_scores(dealer_hand)
    print(f"Your final hand: {player_hand}, final score: {user_score}.")
    print(f"Computer had: {dealer_hand}, final score: {dealer_score}.")
    print(compare(user_score,dealer_score))

while input("Do you want to play Blackjack aka 21? Type 'y' or 'n'.\n") == "y":
    play_game()