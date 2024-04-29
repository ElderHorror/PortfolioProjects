from tkinter import *

window = Tk()

# Change Title
window.title("My first GUI")
window.minsize(width=500, height=300)


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


# Label
my_label = Label(text="I am a label", font=("Arial", 24, 'bold'))
my_label.grid(column=0, row=0)
# my_label.place(x=100, y=100)
# my_label.pack()
# my_label.pack(side="left")

my_label['text'] = 'New Text'
my_label.config(text="New Text")

# Entry
input = Entry(width=10,)
input.insert(END, "Scribble")
input.grid(column=1, row=2)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)


window.mainloop()


