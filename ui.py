THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
from tkinter import *
from quiz_brain import QuizBrain

class GUI():
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        #Window
        self.window = Tk()
        self.window.title = ("QUIZ")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        #Label
        self.score_label = Label(text=f"Score: {self.quiz.score}/{self.quiz.question_number}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        #Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.text = self.canvas.create_text(150, 125, width=280, text="init", font=FONT)
        #Buttons
        correct_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")
        self.true_but = Button(image=correct_img, highlightthickness=0, command=self.true_button_pressed)
        self.true_but.grid(row=2, column=0)
        self.false_but = Button(image=wrong_img, highlightthickness=0, command=self.false_button_pressed)
        self.false_but.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}", fg="white", bg=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.text, text=f"No more question left! Your score is: {self.quiz.score}/{self.quiz.question_number}")
            self.false_but.config(state="disable")
            self.true_but.config(state="disable")
        

    def true_button_pressed(self):
        is_true = self.quiz.check_answer("true")
        self.give_feedback(is_true)

    def false_button_pressed(self):
        is_true = self.quiz.check_answer("false")
        self.give_feedback(is_true)

    def give_feedback(self, correct):
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
