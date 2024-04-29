from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

df = pd.read_csv("data/french_words.csv")
to_learn = df.to_dict(orient="records")
word = {}
known_words = {}
count = 0


def time_up():
    global word
    canvas.itemconfig(image_id, image=flip_card)
    canvas.itemconfig(label1, text="English", fill="WHITE")
    canvas.itemconfig(label2, text=word["English"], fill="WHITE")

def card_change():
    global word, change_time
    window.after_cancel(change_time)
    word = random.choice(to_learn)
    canvas.itemconfig(image_id, image=card)
    canvas.itemconfig(label1, text="French", fill="BLACK")
    canvas.itemconfig(label2, text=word["French"], fill = "BLACK")
    change_time = window.after(3000, time_up)

def remove_card():
    global count
    card_change()

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
change_time = window.after(1000, func=card_change)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=card_change, bg=BACKGROUND_COLOR)
check = PhotoImage(file="images/right.png")
right_button = Button(image=check, highlightthickness=0, command=remove_card, bg=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=2)
right_button.grid(column=1, row=2)

card = PhotoImage(file="images/card_front.png")
flip_card = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
image_id = canvas.create_image(400, 253, image=card)  # Store the returned ID
canvas.grid(column=0, row=0, columnspan=2)


# label1 = Label(text="French", bg="WHITE", font=("Ariel", 40, "italic"))
# label2 = Label(text="trauve", bg="WHITE", font=("Ariel", 60, "bold"))
# label1.place(x=320,y=150)
# label2.place(x=290, y=250)
label1 = canvas.create_text(400, 150, text="", fill="BLACK", font=("Ariel", 40, "italic"))
label2 = canvas.create_text(400, 263, text="", fill="BLACK", font=("Ariel", 60, "bold"))

card_change()

window.mainloop()
