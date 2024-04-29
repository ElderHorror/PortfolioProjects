import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# To use JSON, You have to import the JSON Module
import json

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = []

    for i in range(0, nr_letters):
        letter = random.choice(LETTERS)
        password_list.append(letter)
    for i in range(0, nr_symbols):
        symbols = random.choice(SYMBOLS)
        password_list.append(symbols)
    for i in range(0, nr_numbers):
        numbers = random.choice(NUMBERS)
        password_list.append(numbers)
    random.shuffle(password_list)
    password = "".join(password_list)
    print(password)
    pass_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }}

    # messagebox.showinfo(title="Title", message="Message"
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any boxes empty")
    else:
        # file.write(f"{website} | {email} | {password}\n")
        # To write to a JSON File we use JSON.dump
        # json.dump(new_data, file, indent=4)
        # To read you use JSON.load
        # data = json.load(file)
        try:
            with open("data.json", mode="r") as file:
                # To update the JSON data
                #read old data
                data = json.load(file)
        except FileNotFoundError and json.decoder.JSONDecodeError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as file:
                # Save updated data
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)

def find_password():
    search_site = web_input.get()
    try:
        with open("data.json") as file:
            # To update the JSON data
            # read old data
            data = json.load(file)
    except FileNotFoundError and json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message= "No data file found.")
    else:
        if search_site in data:
            email = data[search_site]["email"]
            password = data[search_site]["password"]
            messagebox.showinfo(title="Saved Website", message=f"Email: {email}\n password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_site} exists.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)


# label
label1 = Label(text="Website:")
label2 = Label(text="Email/Username:")
label3 = Label(text="Password:")
label1.grid(column=0, row=1)
label2.grid(column=0, row=2)
label3.grid(column=0, row=3)


# Entry
web_input = Entry(width=35)
email_input = Entry(width=35)
pass_input = Entry(width=21)
web_input.focus()
email_input.insert(0, "dejispark@gmail.com")
web_input.grid(column=1, row=1, columnspan=2)
email_input.grid(column=1, row=2, columnspan=2)
pass_input.grid(column=1, row=3)


# Button
generate_btn = Button(text="Generate Password", command=generate_password, width=14)
add_btn = Button(text="Add", width=36, command=add_password)
search_btn = Button(text="Search", width=14, command=find_password)
generate_btn.grid(column=3, row=3)
add_btn.grid(column=1, row=4, columnspan=2)
search_btn.grid(column=3, row=1)
window.mainloop()
