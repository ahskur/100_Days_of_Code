from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------- Flashcard Logic ---------- #
# The following code tries to get hold of a file called 'words_to_learn.csv' which will be existent
# if the user has already used the flashcard app
# If the file is not present, it the proceeds to look for a words list
words_to_learn = {}

try:
    word_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    preloaded_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = preloaded_data.to_dict(orient="records")
else:
    words_to_learn = word_data.to_dict(orient="records")

# Open word list with Pandas and save to variable
word_data = pandas.read_csv("data/french_words.csv")
# Create a dictionary using pandas
words_to_learn = word_data.to_dict(orient='records')
# Debug print
# print(words_to_learn)

# Now pick a random word from the file using random choice
# random_word_french = word_data["French"][random.randint(0,101)]

# ---------- Function ---------- #
# Create an empty dictionary to save the current word, so the French and english can be accessed simultaneously
random_word = {}


def pass_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(words_to_learn)
    # Debug print
    # print(random_word["French"])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_word["French"], fill="black")
    canvas.itemconfig(flashcard_background, image=flashcard_front)
    # Wait 3 seconds to flip card if no button is pressed
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    # Show English word for the front card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word["English"], fill="white")
    canvas.itemconfig(flashcard_background, image=flashcard_back)


def is_know():
    # This functions removes the word from the dictionary if the user presses the green button,
    # stating that he already knows the word
    words_to_learn.remove(random_word)
    pass_card()
    # Create a new dataframe from the words to learn list
    know_word_list = pandas.DataFrame(words_to_learn)
    # And save the 'words_to_learn' dictionary to a csv - So the user can use the csv
    # to see which words they still don't know
    # And does't include word index when saving to csv (index = word number in the dictionary)
    know_word_list.to_csv("data/words_to_learn.csv", index=False)

# -------------------- UI -------------------- #

# --- Window Setup --- #

window = Tk()
window.title("Le Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# Wait 3 seconds to flip card if no button is pressed
flip_timer = window.after(3000, func=flip_card)

# --- Flashcard --- #

canvas = Canvas(height=526, width=800)
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
flashcard_background = canvas.create_image(400, 263, image=flashcard_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400,150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 48, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# --- Buttons --- #

right_button_png = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_png, highlightthickness=0, command=pass_card)
right_button.grid(row=1, column=1)

wrong_button_png = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_png, highlightthickness=0, command=is_know)
wrong_button.grid(row=1, column=0)

# Generate a first card after opening the game
pass_card()

# Keeps window open
window.mainloop()