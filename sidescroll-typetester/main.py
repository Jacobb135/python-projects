from tkinter import *
from wonderwords import RandomSentence
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)
gui = Tk()
gui.geometry("800x800")
gui.title("Typing Test")
gui.option_add("*Label.Font", "consolas 30")
gui.option_add("*Button.Font", "consolas 30")


def key_press(event=None):
    try:
        if event.char.lower() == label_right.cget('text')[0].lower():
            label_right.configure(text=label_right.cget('text')[1:])
            label_left.configure(text=label_left.cget('text') + event.char.lower())
            current_letter_label.configure(text=label_right.cget('text')[0])
    except TclError:
        pass


def reset_typing_words():
    s = RandomSentence()
    sentence_array = []
    for _ in range(24):
        sentence = s.simple_sentence()
        sentence_array.append(str(sentence))
        sentences = " ".join(sentence_array)
    text = sentences

    split_point = 0
    global label_left
    label_left = Label(gui, text=text[0:split_point], fg='grey')
    label_left.place(relx=.5, rely=.5, anchor=E)

    global label_right
    label_right = Label(gui, text=text[split_point:])
    label_right.place(relx=.5, rely=.5, anchor=W)

    global current_letter_label
    current_letter_label = Label(gui, text=text[split_point], fg='grey')
    current_letter_label.place(relx=.5, rely=.6, anchor=N)

    global time_left_label
    time_left_label = Label(gui, text=f"0 Seconds", fg='grey')
    time_left_label.place(relx=.5, rely=.4, anchor=S)

    global writeable
    writeable = True
    gui.bind('<Key>', key_press)

    global passed_seconds
    passed_seconds = 0

    gui.after(30000, stop_test)
    gui.after(1000, add_second)


def stop_test():
    global writeable
    writeable = False

    amount_words = len(label_left.cget('text').split(' '))

    time_left_label.destroy()
    current_letter_label.destroy()
    label_right.destroy()
    label_left.destroy()


    global result_label
    result_label = Label(gui, text=f'Words per Minute: {amount_words * 2}', fg='black')
    result_label.place(relx=0.5, rely=0.4, anchor=CENTER)

    global result_button
    result_button = Button(gui, text=f'Retry', command=restart)
    result_button.place(relx=0.5, rely=0.6, anchor=CENTER)


def restart():
    result_label.destroy()
    result_button.destroy()
    reset_typing_words()


def add_second():
    global passed_seconds
    passed_seconds += 1
    time_left_label.configure(text=f'{passed_seconds} Seconds')

    # call this function again after one second if the time is not over.
    if writeable:
        gui.after(1000, add_second)

reset_typing_words()
gui.mainloop()
