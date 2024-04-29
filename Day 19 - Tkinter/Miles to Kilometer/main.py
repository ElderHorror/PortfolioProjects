from tkinter import *

window = Tk()
window.config(padx=100)
window.title("Miles to Km Converter")
window.minsize(width=300,height=100)

# Function
def button_clicked():
    m = int(input1.get())
    km = round(m * 1.609)
    label4.config(text=km)

# Label
label1 = Label(text="Miles", font=("Arial", 10))
label1.grid(column=2,row=0)
label2 = Label(text="is equal to", font=("Arial", 10))
label2.grid(column=0,row=1)
label3 = Label(text="Km", font=("Arial", 10))
label3.grid(column=2,row=1)
label4 = Label(text=0, font=("Arial", 10))
label4.grid(column=1, row=1)

# Entry
input1 = Entry(width=20)
input1.grid(column=1, row=0)


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)




window.mainloop()
