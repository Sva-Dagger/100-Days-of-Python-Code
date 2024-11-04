from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #Easy_Level
    Letters = [choice(letters) for _ in range(randint(8, 10))]
    Symbols = [choice(symbols) for _ in range(randint(2, 4))]
    Numbers = [choice(numbers) for _ in range(randint(2, 4))]

    Password_list = Letters + Symbols + Numbers
    shuffle(Password_list)
    Password = "".join(Password_list)
    Password_input.insert(0, Password)
    pyperclip.copy(Password)

# ---------------------------- Search and Find_Password ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Details for {website} exists.")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = Email_username_input.get()
    password = Password_input.get()
    new_data = {
        website:{"Email" : email,
                "Password":password,
        }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Make sure you haven't left any field left.")
    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            Password_input.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manaer")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1,)

Email_username_label = Label(text="Email/Username:")
Email_username_label.grid(column=0, row=2)

Password_label = Label(text="Password:")
Password_label.grid(column=0, row=3)

website_input = Entry(width=40)
website_input.grid(column=1, row= 1)

Email_username_input = Entry(width=55)
Email_username_input.grid(column=1, row=2, columnspan=2)
Email_username_input.insert(0, "sivam4266@gmail.com")

Password_input = Entry(width=38)
Password_input.grid(column=1, row=3)

Generate_button = Button(text="Generate Password", command=generate_password)
Generate_button.grid(column=2, row=3)

Add_button = Button(width=35, text="Add", command=save)
Add_button.grid(column=1,)

search_button = Button(width=10, text="Search", command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()