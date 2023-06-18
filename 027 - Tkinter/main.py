import tkinter
# Tkinter comes preinstalled with every python version
window = tkinter.Tk()
window.title("My First GUI")
# Minimum size of the window when it's generated
window.minsize(width=500, height=300)
window.config(pady=70)

# Label

my_label = tkinter.Label(text="Well, hello there!", font=("Courier",24,"bold"))
# Specify how the component will appear in the screen
# my_label.pack(side="top")
# my_label.place(x=100,y=250)
my_label.grid(column=0,row=0)


# Button
def button_clicked():
    # my_label["text"]= "Yeaaah, clickty-clackty button!"
    my_label["text"] = input.get()


button = tkinter.Button(text="I'm a button!", command=button_clicked)
# button.pack()
button.grid(column=1,row=2)
button2 = tkinter.Button(text="Bottom text")
button2.grid(column=2, row=0)

# Entry

input = tkinter.Entry(width=70)
input.get()
input.grid(column=5,row=3)
# input.pack()


# Keeps the window open as long as the program is running
window.mainloop()