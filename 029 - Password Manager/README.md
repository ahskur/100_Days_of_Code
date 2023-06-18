# MyPass - Password Manager

This repository contains a simple password manager application built using Python's tkinter library. The application allows you to generate strong passwords and save them with associated website and email/username details.

## Features

- Generate strong passwords with random combinations of letters, numbers, and symbols.
- Save passwords along with the corresponding website and email/username details.
- Display a message box to confirm password saving and prevent empty fields.

## Requirements

To run the application, ensure you have the following installed:

- Python 3.x
- tkinter module

## Usage

1. Clone the repository to your local machine or download the source code.
2. Make sure you have Python 3.x installed on your system.
3. Install the required modules by running the following command:
   ```bash
   pip install tkinter
   ```
4. Run the application using the following command:
   ```bash
   python main.py
   ```

## Code Overview

The main functionality of the application is divided into the following sections:

- **Password Generator**: This section generates a strong password by randomly combining letters, numbers, and symbols. The generated password is displayed in the password entry box.

- **Save Passwords**: This section saves the entered website, email, and password details into a file named `data.txt`. It also performs validation checks to ensure that the required fields are not empty.

- **UI Setup**: This section sets up the user interface using tkinter. It includes creating the main window, displaying the logo, and configuring labels, entry boxes, and buttons.
