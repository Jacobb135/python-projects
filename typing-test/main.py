from tkinter import *
from wonderwords import RandomSentence
import keyboard

s = RandomSentence()
random_list = []


def random_words():
    for _ in range(4):
        words = s.sentence()
        random_list.append(words)

def click(key):
    print(key.char)


def typing_game():
    game_words = text_box.get("1.0", END)
    print(game_words)
    game_on = True
    while game_on:
        for _ in range(len(game_words)):
            if click == game_words:
                print(True)


random_words()
words = ' '.join(str(word) for word in random_list)
window = Tk()
window.title("Typing Test")
window.minsize(width=800, height=800)
text_box = Text(window, height=20, width=55)
sentence_label = Label(window, text="Typo Tester")
sentence_label.config(font=("Arial", 25))
text_entry = Entry(window)
quit_button = Button(window, text="Quit", command=window.quit)
start_button = Button(window, text="Start Typing", command=typing_game)


sentence_label.pack()
text_box.pack()
text_box.insert(END, words)
text_entry.pack()
quit_button.pack()
start_button.pack()

text_entry.bind("<Key>", click)
window.mainloop()
