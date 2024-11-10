from tkinter import *

window = Tk()
window.config(padx=100, pady=200)


window.title("My first GUI programme")
window.minsize(width=500, height=300)
my_lable = Label(text="I am a Label", font=("Arial", 20, "bold"))
my_lable.grid(column=0, row=2)
my_lable["text"] = "New_text"
my_lable.config(padx=50, pady=30)
my_lable.grid()
#Button

def button_clicked():
    New_text = input.get()
    my_lable.config(text=New_text)


button = Button(text = "click me1", command=button_clicked)
button.grid(column=0, row=2)

New_button = Button(text = "New_Button", command=button_clicked)
New_button.grid(column=2, row=0)

#Entry

input = Entry(width=20)
input.grid(column=10, row=10)
input.get()











window.mainloop()