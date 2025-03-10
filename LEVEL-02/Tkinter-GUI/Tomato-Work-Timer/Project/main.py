from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #title_label "timer"
    title_label.configure(text="timer")
    #reset reset_checkmarks
    check_marks.configure(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    # if it is the 8th rep:
    if reps % 8 == 0:
        #red
        count_down(long_break_sec)
        title_label.configure(text="Long Break", fg=RED)
    # if it is the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        #Pink
        count_down(short_break_sec)
        title_label.configure(text="Short Break", fg=PINK)
    # if it is the 1st/3rd/5th/7th rep:
    else:
        #Green
        count_down(work_sec)
        title_label.configure(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/69)
    count_sec = (count % 60)
    if count_sec < 10:
       count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.configure(text = marks)


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
title_label = Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 45, "bold"))
title_label.grid(column=1, row=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


Start_button = Button(text="Start", command=start_timer)
Start_button.grid(column=0, row=2)
Reset_button = Button(text="Reset", command=timer_reset)
Reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_marks.grid(column=1, row=3)








window.mainloop()