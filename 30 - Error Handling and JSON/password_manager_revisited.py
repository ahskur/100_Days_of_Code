import tkinter
from tkinter import *
# Message Box is another module, not a class, therefore not imported by *
from tkinter import messagebox
import random
import json

# ----------- Password Generator ----------- #
def generate_pass():
    password_box.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    # Join all lists together with a "" separating them
    password = "".join(password_list)

    password_box.insert(0, password)


# ----------- Save Passwords ----------- #
def save_pass():
    website = website_box.get()
    email = email_box.get()
    password = password_box.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="There are empty fields.")

    else:
        try:
            with open("data.json", "r") as password_data:
                # We'll be learning how to handle json file
                # Firstly - Read the old data that's stored - OPEN FILE AS READ MODE ONLY!
                data = json.load(password_data)

        except FileNotFoundError:
            with open("data.json", "w") as password_data:
                json.dump(new_data,password_data, indent=4)

        else:
            # Now UPDATE this 'old data' with fresh inputted data
            data.update(new_data)

            # Now after updating data we save the fresh updated data - OPEN FILE AS WRITE MODE!
            with open("data.json","w") as password_data:
                # Saving updated data
                json.dump(data, password_data, indent=4)

        finally:
            website_box.delete(0, END)
            email_box.delete(0, END)
            password_box.delete(0, END)

# ----------- Search Password ----------- #



# ----------- UI Setup ----------- #

# ----- Window setup ----- #
window = tkinter.Tk()
window.title("MyPass - Password Manager")
window.config(padx=50, pady=50)

# ----- Logo ----- #
canvas = tkinter.Canvas(height=200, width=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# ----- Label ----- #

# Website
website_label = tkinter.Label()
website_label.config(text="Website:")
website_label.grid(row=1, column=0)

# Username or Email
l = tkinter.Label()
l.config(text="Email/Username:")
l.grid(row=2, column=0)

# Password
password_label = tkinter.Label()
password_label.config(text="Password:")
password_label.grid(row=3, column=0)

# ----- Entry Boxes ----- #

# Website
website_box = tkinter.Entry(width=55)
website_box.grid(row=1, column=1, columnspan=2)
website_box.focus()

# Email
email_box = tkinter.Entry(width=55)
email_box.grid(row=2, column=1, columnspan=2)

# Password
password_box = tkinter.Entry(width=34)
password_box.grid(row=3, column=1, columnspan=1)

# ----- Buttons ----- #

# Generate Password
generate_password = tkinter.Button()
generate_password.config(text="Generate Password", command=generate_pass)
generate_password.grid(row=3, column=2)

# Add Password
add_password = tkinter.Button()
add_password.config(text="Add Password", width=48, command=save_pass)
add_password.grid(row=4, column=1, columnspan=2)

## Keep window running
window.mainloop()
