Typing Test

Typing Test is a Python program that provides a simple GUI for users to practice their typing skills. The program utilizes the Tkinter module to create the GUI and the wonderwords module to generate random sentences for the user to type.
Requirements

    Python 3.x
    Tkinter module
    wonderwords module

Usage

To run the program, navigate to the directory where the typing_test.py file is located and run the following command in the terminal:

python typing_test.py

Once the program is running, a window titled "Typing Test" will appear. The user will have 30 seconds to type as many words as possible from a randomly generated sentence. The left label is greyed out and will fill in as the user types the correct letters in the right label. A label displaying the current letter to be typed is also present, along with a label showing the time left to type.

The program listens for key presses, and if the pressed key matches the first character in the right label, it removes that character from the right label and adds it to the left label. If the key pressed does not match the first character, nothing happens.

After 30 seconds, the program will display the user's typing speed in words per minute, along with a "Retry" button that the user can click to start a new typing test.
License

This program is licensed under the MIT License - see the LICENSE file for details.
