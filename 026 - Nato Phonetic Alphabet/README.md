# NATO Phonetic Alphabet Converter

This repository contains a Python script that converts words into their equivalent phonetic code words using the NATO Phonetic Alphabet. The script utilizes the pandas library to read a CSV file containing the NATO phonetic alphabet mapping.

## Features

- Converts words into NATO phonetic code words.
- Maps each letter of the word to its corresponding phonetic code word.
- Handles user input and provides the converted phonetic code words as output.

## Requirements

To run the script, ensure you have the following installed:

- Python 3.x
- pandas library

## Usage

1. Clone the repository to your local machine or download the source code.
2. Make sure you have Python 3.x installed on your system.
3. Install the required libraries by running the following command:
   ```bash
   pip install pandas
   ```
4. Prepare the input data:
   - Create a CSV file named `nato_phonetic_alphabet.csv`.
   - Format the CSV file with two columns: `letter` and `code`, representing the letter and its corresponding phonetic code word.
   - Populate the CSV file with the NATO phonetic alphabet mapping.
5. Run the script using the following command:
   ```bash
   python main.py
   ```
6. Follow the prompts to enter a word for conversion.
7. The script will output the phonetic code words corresponding to each letter of the input word.

## Note

Make sure to provide the appropriate `nato_phonetic_alphabet.csv` file with the correct mapping of letters and phonetic code words.
