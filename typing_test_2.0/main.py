import tkinter as tk
import threading
import time
from random_words import random_words


class TypingTest:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Typing Speed App")
        self.window.geometry("800x600")
        self.window.config(bg="black")

        self.title = tk.Label(self.window, text="Typing Speed App")
        self.title.config(font=("Arial", 25))

        self.frame = tk.Frame(self.window, bg="black")

        self.text_to_type = tk.Label(self.frame, fg="white", bg="black", text=random_words(),
                                     wraplength=500, justify="center", font=("Consolas", 16))
        self.text_to_type.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.input_field = tk.Entry(self.frame, width=45, font=("Consolas", 20))
        self.input_field.grid(row=1, column=0, columnspan=2, padx=5, pady=15)
        self.input_field.bind("<KeyPress>", self.start)

        self.wpm_field = tk.Label(self.frame, bg="black", fg="white", text="Speed: 0 WPM", font=("Consolas", 16))
        self.wpm_field.grid(row=2, column=0, columnspan=2, padx=5, pady=15)

        self.high_score_field = tk.Label(self.frame, bg="black", fg="white", text="Highest score: 0 WPM", font=("Consolas", 16))
        self.high_score_field.grid(row=3, column=0, columnspan=2, padx=5, pady=15)

        self.reset_button = tk.Button(self.frame, bg="black", fg="white", text="Reset", command=self.reset)
        self.reset_button.grid(row=4, column=0, columnspan=2, padx=5, pady=15)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False
        self.wpm_count = tk.StringVar()
        self.read_highscore()
        self.window.mainloop()

    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                timing = threading.Thread(target=self.timer)
                timing.start()
        if not self.text_to_type.cget('text').startswith(self.input_field.get()):
            self.input_field.config(fg="red")
        else:
            self.input_field.config(fg="black")
        if self.input_field.get() == self.text_to_type.cget('text')[:-1]:
            self.running = False
            self.input_field.config(fg="green")


    def timer(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            wpm = round(len(self.input_field.get()) / 5 / self.counter * 60)
            self.wpm_field.config(text=f"Speed: {wpm} WPM")

            try:
                with open("high_score.txt", "r") as file:
                    self.previous_highscore = file.read()
                    self.high_score_field.config(text=f"Highest score: {self.previous_highscore} WPM")
            except IOError:
                file = open("high_score.txt", "w+")
                file.write('%d' % 0)
                self.previous_highscore = file.read()

        if wpm > int(self.previous_highscore):
            print(wpm)
            print(self.previous_highscore)
            with open("high_score.txt", "w") as file:
                file.write('%d' % wpm)
                self.high_score_field.config(text=f"Highest Score: {wpm} WPM")

    def reset(self):
        self.running = False
        self.counter = 0
        self.wpm_field.config(text="Speed: 0 WPM")
        self.text_to_type.config(text=random_words())
        self.input_field.delete("0", tk.END)

    def read_highscore(self):
        try:
            with open("high_score.txt", "r") as file:
                self.previous_highscore = file.read()
                self.high_score_field.config(text=f"Highest score: {self.previous_highscore} WPM")
        except IOError:
            file = open("high_score.txt", "w+")
            file.write('%d' % 0)
            self.previous_highscore = file.read()

TypingTest()




