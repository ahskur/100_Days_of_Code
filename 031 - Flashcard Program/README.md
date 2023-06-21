# Le Flashcard App

Le Flashcard App is a simple flashcard application that helps you learn new words in a foreign language. This application displays French words and their English translations, allowing you to test your knowledge and practice vocabulary. With Le Flashcard App, you can easily flip between the French and English words and mark words as "known" once you've mastered them.

## Features

- **Flashcard Logic**: The application loads a list of words from a CSV file and presents them as flashcards. The words can be in French and their corresponding English translations.
- **Word Progress**: You can mark words as "known" if you are familiar with them, and they will be removed from the flashcard rotation.
- **Persistence**: The application saves your progress by updating a CSV file with the remaining words to learn. This allows you to continue your learning journey from where you left off.

## Usage

1. Launch the Le Flashcard App.
2. The application will display a flashcard with a French word.
3. Try to recall the English translation of the word.
4. Click the right button if you know the word, or the wrong button if you need more practice.
5. If you click the right button, the word will be marked as "known" and removed from future flashcards.
6. The application will automatically display the next flashcard with a new word.
7. Continue the process of recalling and marking words until you have mastered the vocabulary.

## Requirements

- Python 3.x
- `tkinter` module
- `pandas` module

## Installation

1. Clone this repository to your local machine or download the code as a ZIP file.
2. Make sure you have Python 3.x installed on your system.
3. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Customization

- Place your own words list in the `data/french_words.csv` file. Make sure the CSV file contains named columns for each word and its translations.
- You can replace the flashcard front and back images with your own images in the `images/` directory, using the filenames `card_front.png` and `card_back.png`.
- Customize the application's appearance and layout by modifying the code in the UI section.
