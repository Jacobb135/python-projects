from morse import morse
from art import logo

print(logo)
print("MORSE CODE TRANSLATOR")

end_program = False
while not end_program:
    string_to_decode = input("Please enter a word to translate or type q! to quit. \n").upper()
    if string_to_decode == 'Q!':
        end_program = True
        break
    try:
        morse_list = [morse[letter] for letter in string_to_decode]
    except KeyError:
        print('Sorry you have entered an invalid character')
    else:
        print(morse_list)

