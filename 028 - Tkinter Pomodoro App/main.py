import tkinter
import math


# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPETITION = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(TIMER)
    timer_label.config(text="Pomodoro\nTimer",fg="GREEN", font=(FONT_NAME, 38, "bold"), highlightthickness=0, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    global REPETITION
    REPETITION = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


# Functions - For each button
def start_timer():
    global REPETITION
    REPETITION += 1

    # Transform minutes to seconds for each work time or pause (short or long) time
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Check for the amount of repetitions using Modulo so we know when it's pause time
    if REPETITION % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK\nTIME", fg=RED)

    elif REPETITION % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK\nTIME", fg=PINK)
    else:
        timer_label.config(text="WORK\nTIME", fg="GREEN", font=(FONT_NAME, 38, "bold"), highlightthickness=0, bg=YELLOW)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    # Format seconds so it always show --:00 or --:03 etc
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
       global TIMER
       TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(REPETITION/2)):
            marks += "✔"
        checkmark.config(text=f"{marks}")

# ---------------------------- UI SETUP ------------------------------- #


# Window
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.minsize(height=500,width=550)
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas - Tomato Image
canvas = tkinter.Canvas(height=225,width=200, bg=YELLOW, highlightthickness=0)
pomodoro = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Labels
timer_label = tkinter.Label()
timer_label.config(text="Pomodoro\nTimer",fg="GREEN", font=(FONT_NAME, 38, "bold"), highlightthickness=0, bg=YELLOW)
timer_label.grid(column=1, row=0)

checkmark = tkinter.Label()
checkmark.config(text="", fg=GREEN, bg=YELLOW, background=YELLOW, borderwidth=0, font=(FONT_NAME, 30, "normal"))
checkmark.grid(column=1,row=4)

# Buttons
start_button = tkinter.Button()
start_button.config(text="Start",font=(FONT_NAME, 12, "normal"), highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=3)

reset_button = tkinter.Button()
reset_button.config(text="Reset", font=(FONT_NAME, 12, "normal"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=3)


window.mainloop()