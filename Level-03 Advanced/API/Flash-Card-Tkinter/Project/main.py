from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def Next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(Card_title, text="French", fill="black")
    canvas.itemconfig(Card_word, text = current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(Card_title, text="English", fill="white")
    canvas.itemconfig(Card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data =pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    Next_card()



window = Tk()
window.title("Flashy")
flip_timer = window.after(3000, func=flip_card)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width = 800, height= 526)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400,263, image=card_front_img)
Card_title = canvas.create_text(400, 150, text="", font=("Ariel",40,"italic"))
Card_word = canvas.create_text(400, 263, text="", font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=1)

cross_image=PhotoImage(file="wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=Next_card)
unknown_button.config(padx=50, pady=50)
unknown_button.grid(row=1, column=0)

right_image= PhotoImage(file="right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.config(padx=50, pady=50)
known_button.grid(row=1, column=2)

Next_card()

window.mainloop()