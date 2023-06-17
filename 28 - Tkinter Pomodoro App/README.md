# Pomodoro Timer

This repository contains a Pomodoro Timer application implemented using Python's tkinter library. The Pomodoro Technique is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.

## Features

- Set work time, short break time, and long break time.
- Display a countdown timer for each interval.
- Automatically switch between work time and break time intervals.
- Keep track of completed work and break intervals with checkmarks.

## Requirements

To run the application, ensure you have the following installed:

- Python 3.x
- tkinter module
- math module

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

- **Timer Reset**: This section contains a function to reset the timer and clear any ongoing intervals.

- **Timer Mechanism**: This section contains the `start_timer` function, which handles the logic of starting the timer and determining the current interval (work time, short break, or long break). It also updates the timer label accordingly.

- **Countdown Mechanism**: This section contains the `count_down` function, which performs the countdown for each interval. It updates the canvas with the remaining time and checks if the countdown has reached zero to switch to the next interval.

- **UI Setup**: This section sets up the user interface using tkinter. It includes creating the main window, displaying the tomato image using a canvas, configuring labels, and creating start and reset buttons.
