import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(height=100, width=300)
window.config(padx=60, pady=25)

# Labels

miles_text = tkinter.Label(text="Miles")
miles_text.grid(column=2, row=0)

equal_to = tkinter.Label(text="is equal to")
equal_to.grid(column=0, row=1)

value_in_km = tkinter.Label(text="")
value_in_km.grid(column=1, row=1)

km_text = tkinter.Label(text="Km")
km_text.grid(column=2, row=1)

# Entry

miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)


# Button
def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    value_in_km.config(text=f"{km}")


calc_button = tkinter.Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)

# Keeps program running
window.mainloop()