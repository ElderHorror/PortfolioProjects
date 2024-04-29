from tkinter import *

window = Tk()

# Change Title
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, 'bold'))
my_label.pack()
# my_label.pack(side="left")

my_label['text'] = 'New Text'
my_label.config(text="New Text")



#Entry

input = Entry(width=10,)
input.pack()
input.insert(END, "Scribble")


#Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    print(text.get("1.0",END))

button = Button(text="Click Me", command=button_clicked)
button.pack()


#Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


#Text box
text = Text(height=5,width=30)

#Puts cursor in text box
text.focus()
text.insert(END,"New textbox")
print(text.get("1.0", END))
text.pack()


#Scale
#Called with current sclae value
def scale_used(value):
    print(value)
scale = Scale(from_=0,to=100,command=scale_used)
scale.pack()


#Checkbox
def checkbox_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbox_used)
checked_state.get()
checkbutton.pack()


#Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1",value=1,variable=radio_state,command=radio_used)
radiobutton2 = Radiobutton(text="Option2",value=2,variable=radio_state,command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

window.mainloop()
