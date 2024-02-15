THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
from tkinter import *

class GUI():
    def __init__(self):
        #Window
        self.window = Tk()
        self.window.title = ("QUIZ")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        #Label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        #Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.text = self.canvas.create_text(150, 125, text="init", font=FONT)
        #Buttons
        correct_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")
        self.true_but = Button(image=correct_img, highlightthickness=0)
        self.true_but.grid(row=2, column=0)
        self.false_but = Button(image=wrong_img, highlightthickness=0)
        self.false_but.grid(row=2, column=1)
        self.window.mainloop()

    def change_question(self, add_question):
        self.canvas.itemconfig(self.text, text=add_question)