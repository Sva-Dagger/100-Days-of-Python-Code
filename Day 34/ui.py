from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface :
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.Score_label = Label(text=f"score: 0", fg = "white", bg= THEME_COLOR )
        self.Score_label.grid(column=1, row=0)

        self.canvas = Canvas(width= 300, height=250, bg="white")
        self.Question_text = self.canvas.create_text(150, 125, width=280,
                                                     text="Some Question text",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.right_button_label = Button(image= self.true_img, highlightthickness=0, command=self.true_pressed)
        self.right_button_label.grid(column= 0, row=2)

        self.false_img = PhotoImage(file="images/false.png")
        self.wrong_button_label = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.wrong_button_label.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.Score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.Question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.Question_text, text="You reached the end of the text.")
            self.right_button_label.config(state="disabled")
            self.wrong_button_label.config(state="disabled")
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

